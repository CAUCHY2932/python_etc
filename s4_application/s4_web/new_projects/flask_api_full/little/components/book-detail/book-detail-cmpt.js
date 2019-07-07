
import { HTTP } from '../../utils/http.js'
var http = new HTTP()

Component({
  /**
   * 组件的属性列表
   */
  properties: {
    isbn: String
  },
  /**
   * 组件的初始数据
   */
  data: {
    isOpen: 'ellipsis', // 
  },

  /**
   * 组件的方法列表
   */
  methods: {
    onIsOpen(){
      let isOpen = this.data.isOpen ? '' : 'ellipsis';
      this.setData({
        isOpen: isOpen,
      })
      if (isOpen){
        wx.pageScrollTo({
          scrollTop: 0,
          duration: 0
        })
      }else{
        wx.pageScrollTo({
          scrollTop: 300,
          duration: 300
        })
      }
    },
    onTap(event){
      var params = {
        url: 'gift/' + this.data.isbn,
        type: 'POST',
        sCallback: function (data) {
          wx.showToast({
            title: '赠送成功',
            icon: 'success',
            duration: 2000
          })
        },
        eCallback: function (e) {
          console.log(e.data.code)
          if (e.data.error_code == 2001) {
            wx.showToast({
              title: '已添加到礼物清单',
              icon: 'none',
              duration: 2000
            })
          }
          if (e.statusCode == 401 )
           {
            wx.showModal({
              title: '提示',
              content: '未登录，请先登录',
              success: function (res) {
                if (res.confirm) {
                  wx.switchTab({
                    url: '../login/login'
                  })
                } else if (res.cancel) {
                  console.log('用户点击取消')
                }
              }
            })
          }
        }
      }
      http.request(params)
    }
  },

  ready: function () {
    var that = this
    var params = {
      url: 'book/' + this.properties.isbn + '/detail',
      sCallback: function (data) {
        that.setData({
          book: data
        })
      }
    }
    http.request(params)
  }
})
