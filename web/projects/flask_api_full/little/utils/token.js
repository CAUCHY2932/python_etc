// 引用使用es6的module引入和定义
// 全局变量以g_开头
// 私有函数以_开头
import {config} from '../config.js'

class Token {
  constructor() {
    var baseUrl = config.api_base_url;
    this.verifyUrl = baseUrl + 'token/secret';
    this.tokenUrl = baseUrl + 'token';
  }

  verify() {
    var token = wx.getStorageSync('token');
    if (!token) {
      this.getTokenFromServer();
    }
    else {
      this.veirfyFromServer(token);
    }
  }

  veirfyFromServer(token) {
    var that = this;
    wx.request({
      url: that.verifyUrl,
      method: 'POST',
      data: {
        token: token
      },
      success: function (res) {
        if(res.statusCode!=200){
          that.getTokenFromServer();
        }
      }
    })
  }

  getTokenFromServer(callBack) {
    var that = this;
    wx.login({
      success: function (res) {
        wx.request({
          url: that.tokenUrl,
          method: 'POST',
          data: {
            account:res.code,
            type:201
          },
          success: function (res) {
            wx.setStorageSync('token', res.data.token);
            callBack && callBack(res.data.token);
          }
        })
      }
    })
  }
}

export { Token };