解决方案，前方高能

打开External Libraries，这里存放很我们很多导入的包，
找到site-packages->Flask_cache->jinjia2ext,
将33行的from flask.cache import make_template_fragment_key改为
from flask_cache import make_template_fragment_key。
没错就是这么简单，大工告成。
