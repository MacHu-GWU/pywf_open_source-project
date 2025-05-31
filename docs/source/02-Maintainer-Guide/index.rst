Maintainer Guide
==============================================================================
这篇文档是为维护者准备的, 提供了关于如何管理和维护该项目的指南.


Project Background
------------------------------------------------------------------------------
为了理解整个项目架构, 我们首先需要了解这个项目的背景和设计初衷.

`The Ultimate Python Project Development Workflow <https://sanhehu.atlassian.net/wiki/spaces/TECHGARDEN/pages/461242370/The+Ultimate+Python+Project+Development+Workflow>`_ 博文详细介绍了我的 Python Project Development Workflow 在十多年间的进化历程. 而 ``pywf_open_source`` 正是该博文中提到的 ``open_source`` workflow 的具体实现, 专门为发布在 PyPI 上的开源项目量身设计.

接下来让我们了解这个项目的完整架构组成.


Repository Architecture
------------------------------------------------------------------------------
虽然 ``pywf_open_source`` 是 ``open_source`` workflow 自动化逻辑的核心实现, 但完整的解决方案实际上由三个相互关联的 GitHub Repository 组成:

- `pywf_open_source-project <https://github.com/MacHu-GWU/pywf_open_source-project>`_: Automation Library, 实现了核心的自动化逻辑
- `cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source_demo-project>`_: Seed Repository, 作为具体项目示例, 展示了使用 ``open_source`` workflow 的开源项目的标准目录结构和代码实现
- `cookiecutter-pywf_open_source <https://github.com/MacHu-GWU/cookiecutter-pywf_open_source>`_: Cookiecutter Template, 基于种子项目创建的参数化模板, 能够一键生成符合 ``pywf_open_source`` workflow 规范的新项目

这三个 Repository 的协作关系为我们的开发工作流程奠定了基础.


Development Workflow
------------------------------------------------------------------------------
在实际开发过程中, 我们需要同时维护和迭代两个核心模块:

1. 自动化逻辑: 在 `pywf_open_source-project <https://github.com/MacHu-GWU/pywf_open_source-project>`_ Repository 中实现和完善
2. 种子项目: 在 `cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source_demo-project>`_ Repository 中维护和更新

开发过程中, 这两个 Repository 需要保持同步迭代. 当两个 Repository 都达到稳定状态后, 我们再运行 `cookiecutter-pywf_open_source <https://github.com/MacHu-GWU/cookiecutter-pywf_open_source>`_ 中的自动化脚本, 将种子项目打包成可重用的模板.

.. note::

    值得注意的是, ``pywf_open_source-project`` 本身就是一个开源项目, 它采用自身的 ``pywf_open_source`` workflow 进行管理和维护 (这在软件工程中被称为自举 bootstrapping).

为了确保代码质量, 我们采用了完善的测试策略.


Testing Strategy
------------------------------------------------------------------------------
本项目采用测试驱动的开发方式, 通过在测试用例中完整验证所有 workflow 功能来确保代码质量. 由于项目的核心价值在于为其他项目提供开发流程加速, 我们需要通过 ``cookiecutter_pywf_open_source_demo-project`` 种子项目来验证自动化功能的有效性.

因此, 你会在项目根目录下看到完整的种子项目代码: `pywf_open_source-project/cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/pywf_open_source-project/tree/main/cookiecutter_pywf_open_source_demo-project>`_.

核心测试文件 `tests/test_pywf.py <https://github.com/MacHu-GWU/pywf_open_source-project/blob/main/tests/test_pywf.py>`_ 完整模拟了 Python 项目开发的全生命周期, 包括:

- 创建和删除虚拟环境
- 依赖管理 (支持全量安装和分组安装)
- 多种测试类型 (unit test, coverage test, integration test, load test)
- 本地文档构建和预览
- 项目打包和本地预览
- PyPI 发布流程
- GitHub Release 创建
- 自动配置 https://codecov.io 代码覆盖率追踪
- 自动配置 https://readthedocs.org 文档构建
- GitHub Repository 元数据自动更新

测试完成后, 我们需要保持种子项目的同步更新.


Seed Project Sync
------------------------------------------------------------------------------
在种子项目的维护过程中, 有一个重要的原则需要严格遵守: 所有对 ``cookiecutter_pywf_open_source_demo-project`` 种子项目的修改都必须在 Source Repository `cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source_demo-project>`_ 中进行, 因为这里是 Source of Truth.

修改完成后, 需要运行 `sync_cookiecutter_pywf_open_source_demo.py <https://github.com/MacHu-GWU/pywf_open_source-project/blob/main/sync_cookiecutter_pywf_open_source_demo.py>`_ 脚本, 将最新代码同步到测试环境 `pywf_open_source-project/cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/pywf_open_source-project/tree/main/cookiecutter_pywf_open_source_demo-project>`_ 进行验证.

同步完成后, 我们需要对自动化库进行全面测试.


Automation Library Testing
------------------------------------------------------------------------------
随着自动化脚本和种子项目的不断完善, 我们需要频繁地运行 `tests/test_pywf.py <https://github.com/MacHu-GWU/pywf_open_source-project/blob/main/tests/test_pywf.py>`_ 来确保核心功能的稳定性. 测试代码包含许多实际场景的考虑:

- 某些功能依赖 `home_secret.json <https://github.com/MacHu-GWU/home_secret-project>`_ 中的认证信息, 在 CI 环境中不便测试
- 部分功能在 Windows 系统中可能不够稳定
- 涉及改变 SaaS 服务状态的功能在 CI 中需要跳过执行

当 Code Coverage Test 覆盖了所有本地可运行, 无副作用的功能后, 我们就可以认为 Automation Library 达到了稳定状态.

接下来需要在真实环境中验证种子项目的可用性.


Real Seed Repository Environment Testing
------------------------------------------------------------------------------
在自动化库测试完成后, 我们需要将 ``pywf_open_source`` 安装到全局 Python 环境中, 然后使用种子项目进行真实场景测试. 选择全局安装的原因是这个库类似于 poetry, uv 等 Python 环境管理工具, 推荐采用 "一次安装, 到处运行" 的使用模式.

从 `Makefile <https://github.com/MacHu-GWU/pywf_open_source-project/blob/main/cookiecutter_pywf_open_source_demo-project/Makefile>`_ 中可以看到, 大部分自动化命令都使用全局的 ``~/.pyenv/shims/python`` 来执行.

在 `cookiecutter_pywf_open_source_demo-project <https://github.com/MacHu-GWU/cookiecutter_pywf_open_source_demo-project>`_ 种子项目中, 我们需要按照标准流程依次执行所有 ``make`` 命令, 全面验证各项功能. 由于这是测试专用的种子项目, 可以放心地进行版本升级, 避免与 PyPI 和 GitHub Release 中的版本产生冲突.

真实环境测试通过后, 我们就可以进行最终的模板发布.


Cookiecutter Template Release
------------------------------------------------------------------------------
当种子项目的真实环境测试全部通过后, 最后一步就是将其打包为可重用的 Cookiecutter 模板.

具体的打包流程和配置详情, 请参考 `cookiecutter-pywf_open_source <https://github.com/MacHu-GWU/cookiecutter-pywf_open_source>`_ Repository 中的完整文档.