测试是否能工用 subprocess CD 到另一个目录下运行 ``poetry env use``, 看看这个命令能否在正确的位置创建 ``.venv`` 目录.

.. code-block:: bash

    $ cd /path/to/Poetry-Use-Test
    $ python script.py

    Creating virtualenv mypackage in /path/to/01-Poetry-Use-Test/mypackage-project/.venv
    Using virtualenv: /path/to/01-Poetry-Use-Test/mypackage-project/.venv
