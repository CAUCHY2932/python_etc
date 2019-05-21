from django.db import models

# Create your models here.
from blog.models import Post


class Comment(models.Model):

    STATUS_NORMAL = 1
    STATUS_DEL = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEL, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name='评论目标')
    content = models.CharField(max_length=2000, verbose_name='内容')
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'
