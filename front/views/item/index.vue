<template>
  <div class="items">
    <!-- <div>{{ info }}</div>
    <div>{{ printlist }}</div>
    <img :src="srclink" />
    <el-link @click="ask(item)" v-for="item in printlist" :index="item" :key="item">
      {{ item }}
    </el-link> -->
    <el-card v-for="item in list" :key="'list'+item.pk" :body-style="{ padding: '10px' }">
      <el-link type="primary" @click="open(item)">{{item.name}}</el-link>
    </el-card>

    <el-card class="op" id="form">
      <el-form>
        <el-form-item label="Title">
          <el-input v-model="title" placeholder="Please Enter Title" />
        </el-form-item>
        <el-form-item>
          <div v-if="updateData">
            <el-button type="success" @click="editAble = true" v-if="!editAble">Edit</el-button>
            <div v-html="content" v-if="!editAble"></div>
          </div>
          <div style="border: 1px solid #ccc; margin-top: 10px" v-if="!updateData || editAble">
            <Toolbar
              style="border-bottom: 1px solid #ccc"
              ref="tool"
              :editor="editor"
              :defaultConfig="toolbarConfig"
            />
            <Editor
              style="height: 300px; overflow-y: hidden"
              :defaultConfig="editorConfig"
              v-model="content"
              @onCreated="onCreated"
            />
          </div>
        </el-form-item>
        <el-form-item label="Category">
          <el-select v-model="addToType" placeholder="Choose">
            <el-option
              v-for="item in typeList"
              :key="'sel'+item.pk"
              :label="item.name"
              :value="item.pk">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="ocr result" v-if="ocrAttrs.length > 0">
          <el-table :data="ocrAttrs" max-height="300">
            <el-table-column label="attributeName" prop="attribute_name"></el-table-column>
            <el-table-column label="attributeValue" prop="attribute_value"></el-table-column>
          </el-table>
        </el-form-item>
      </el-form>
      <br>
      <el-button @click="submitForm" type="primary">Submit</el-button>
      <el-button @click="resetForm" type="success">Reset</el-button>
      <el-button @click="deletePage" type="danger">Detele</el-button>
    </el-card>

    <el-card>
      Slug: <el-tag>{{slug === '' ? 'no slug' : slug}}</el-tag>
      <div class="ocr">
        <div class="left-cont clearfix">
          <el-image
            v-if="'data:image/png;base64,'!==srclink"
            style="width: 720px; height: 360px; float: left"
            :src="srclink"
          />
          <div style="float: right">
            <el-upload class="upload-demo" drag :on-success="imgReturn" :action="uploadOrcPath" :multiple="false" :before-upload="beforeUpload">
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">Please drag the file, or <em>click here</em> to choose a file</div>
              <div class="el-upload__tip" slot="tip">Only support jpg/png file</div>
            </el-upload>
          </div>
        </div>
        <br>
        <div class="right-cont">
          <el-table :data="ocrData" style="width: 100%">
            <el-table-column v-for="(f,idx) in ocrDataFields" :key="'excel'+f" :prop="f" :label="f" :width="idx<5?'150':'80'">
              <template slot-scope="scope">
                <el-input v-model="ocrData[scope.$index][f]" width="20" size="mini" />
              </template>
            </el-table-column>
          </el-table>
        </div>
        <br>
        <el-button :disabled="ocrData.length === 0" type="primary" @click="submitJson">Upload Modified Content</el-button>
      </div>
    </el-card>
  </div>
</template>

<style scoped>
.items {
  padding: 20px 10px;
  height: 100%;
}
.ocr {
  /* display: flex; */
  width: 100%;
  /* justify-content: space-between; */
}
.left-cont {
  position: relative;
  width: 100%;
}
.el-card {
  margin-bottom: 8px;
}
.el-card.op {
  margin-top: 16px;
}
.clearfix::before, .clearfix::after {
    content: '';
    display: table;
    clear: both;
}
</style>

<script>
import axios from 'axios';
import { Editor, Toolbar} from "@wangeditor/editor-for-vue";
import "@wangeditor/editor/dist/css/style.css";
import { Notification } from 'element-ui';
import { i18nChangeLanguage } from '@wangeditor/editor'

const curName = 'items'
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'items',
  components: { Editor, Toolbar },
  data() {
    return {
      info: null,
      printlist: [],
      indexlist: [],
      srclink: "data:image/png;base64,",
      information: null,
      type: undefined,
      typeName: curName,
      typeList: [],
      list: [],
      ocrPath: 'http://127.0.0.1:8000/wiki/ocr/' + curName,
      title: '',
      slug: '',
      addToType: '',
      content: '',
      updatePk: -1,
      updateData: false,
      editAble: false,
      editor: null,
      toolbarConfig: {
        excludeKeys: ['uploadImage','uploadVideo']
      },
      editorConfig: {
        focus: false,
        MENU_CONF: {},
      },
      ocrData: [],
      ocrDataFields: ['content','as_cat','chunk','cat'],
      ocrAttrs: [],
      attrsCacheMap: {}
    }
  },
  computed: {
    uploadOrcPath() {
      return `${this.ocrPath}/${this.slug}/`
    }
  },
  created() {
    i18nChangeLanguage('en')
    axios
      .get('http://127.0.0.1:8000/wiki/page/')
      .then(res => {
        const types = res.data
        this.typeList = types
        for (let i = 0; i < types.length; i++) {
          if (this.typeName === types[i].name) {
            this.type = types[i].pk
            return
          }
        }
      })
    axios
      .get('http://127.0.0.1:8000/wiki/page/' + this.typeName + '/')
      .then(res => {
        this.list = res.data
      })
  },
  beforeDestroy() {
    const editor = this.editor
    if (editor == null) return
    editor.destroy()
  },
  watch: {
    title(n) {
      this.slug = n.trim().replace(' ', '-')
    }
  },
  methods: {
    imgReturn(res) {
      const data = res.json
      if (data.length > 1) {
        this.ocrData = data.slice(1)
      }
      const imgData = JSON.stringify(res.image).slice(3, -2)
      this.srclink = this.srclink + imgData
    },
    open(item) {
      this.updateData = true
      this.editAble = false
      this.title = item.name
      this.slug = item.name.trim().replace(' ', '-')
      this.content = item.content
      this.addToType = item.type
      this.updatePk = item.pk

      this.ocrAttrs = item.attributes
      window.location.hash = '#form'
      setTimeout(() => {
        window.location.hash = ''
      }, 0)
    },
    resetForm() {
      this.ocrAttrs = []
      this.updateData = false
      this.editAble = false
      this.title = ''
      this.slug = ''
      this.addToType = ''
      this.updatePk = -1
      this.content = ''
    },
    onCreated(editor) {
      this.editor = Object.seal(editor); // 【注意】一定要用 Object.seal() 否则会报错
    },
    submitForm() {
      if (this.slug === '') {
        Notification.warning('Please Enter Title')
        return
      }
      let tn = ''
      for (let i = 0; i < this.typeList.length; i++) {
        if (this.typeList[i].pk === this.addToType) {
          tn = this.typeList[i].name
        }
      }
      const data = {
        name: this.title,
        slug: this.slug,
        content: this.content,
        type: this.addToType
      }
      if (this.updateData) {
        // 更新数据
        const path = `http://127.0.0.1:8000/wiki/page/${tn}/${this.slug}/`
        axios
          .put(path, {...data, pk: this.updatePk})
          .then(res => {
            Notification.success(`${res.data.name} Modify Successfully`)
            axios
              .get('http://127.0.0.1:8000/wiki/page/' + this.typeName + '/')
              .then(res => {
                this.list = res.data
              })
          })
      } else {
        const path = `http://127.0.0.1:8000/wiki/page/${tn}/`
        axios
          .post(path, data)
          .then(res => {
            this.list.push(res.data)
            Notification.success(`Input${this.res.data.name}Successfully`)
            axios
              .get('http://127.0.0.1:8000/wiki/page/' + this.typeName + '/')
              .then(res => {
                this.list = res.data
              })
          })
      }
    },
    beforeUpload() {
      if (this.slug === '') {
        Notification.warning('Please Enter Title')
        return Promise.reject(false)
      }
    },
    submitJson() {
      if (this.slug === '') {
        Notification.warning('Please Enter Title')
        return
      }
      const jsonData = [{"TLX":"TLX","TLY":"TLY","BLX":"BLX","BLY":"BLY","BRX":"BRX","BRY":"BRY","TRX":"TRX","TRY":"TRY","content":"content","p":"p","as_cat":"as_cat","chunk":"chunk","cat":"cat"}]
      jsonData.push(...this.ocrData)
      const path = `http://127.0.0.1:8000/wiki/ocr/${this.typeName}/${this.slug}/response/`
      axios
        .post(path, {json:jsonData})
        .then(res => {
          this.attrsCacheMap[this.slug] = res.data.attributes
          this.ocrAttrs = res.data.attributes
        })
    },
    deletePage() {
      axios.delete(`http://127.0.0.1:8000/wiki/page/${this.typeName}/${this.slug}`).then(res => {
        this.resetForm()
      axios
      .get('http://127.0.0.1:8000/wiki/page/' + this.typeName + '/')
      .then(res => {
        this.list = res.data
      })
      })
    }
  }
}
</script>
