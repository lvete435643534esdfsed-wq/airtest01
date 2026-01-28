import pkgutil
import pocoui

print('pocoui 包路径:', pocoui.__file__)
print('pocoui 包含的模块:')
for _, name, _ in pkgutil.iter_modules(pocoui.__path__):
    print(f'  - {name}')

# 检查是否可以导入poco模块
try:
    import poco
    print('\npoco 模块可以导入!')
    print(f'poco 版本: {poco.__version__}')
except ImportError as e:
    print(f'\npoco 模块导入失败: {e}')
