
import { Token } from 'token.js';
import { config } from '../config.js'
import { base64_encode } from '../utils/base64.js'

class HTTP {
  constructor() {
    this.baseRestUrl = config.api_base_url;
  }

  //http 请求类, 当noRefech为true时，不做未授权重试机制
  request(params) {
    var that = this
    var url = this.baseRestUrl + params.url;

    if (!params.type) {
      params.type = 'GET';
    }
    wx.request({
      url: url,
      data: params.data,
      method: params.type,
      header: {
        'content-type': 'application/json',
        'Authorization': 'Basic ' + base64_encode(
          wx.getStorageSync('token') + ':')
      },
      success: function (res) {

        // 判断以2（2xx)开头的状态码为正确
        // 异常不要返回到回调中，就在request中处理，记录日志并showToast一个统一的错误即可
        var code = res.statusCode.toString();
        var startChar = code.charAt(0);
        if (startChar == '2') {
          params.sCallback && params.sCallback(res.data);
        } else {
          params.eCallback && params.eCallback(res);
        }
      },
      fail: function (err) {
      }
    });
  }
};

export { HTTP };