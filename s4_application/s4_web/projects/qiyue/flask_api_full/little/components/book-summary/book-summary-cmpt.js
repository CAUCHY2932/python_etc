// components/book/book-single-cmpt.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    book: Object
  },
  /**
   * 组件的初始数据
   */
  data: {

  },

  /**
   * 组件的方法列表
   */
  methods: {
    onTap: function (event) {
      var that = this
      wx.navigateTo({
        url:'../../pages/detail/detail?isbn=' + this.properties.book.isbn
      })
      console.log(event)
    }
  }
})
