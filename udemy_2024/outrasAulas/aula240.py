class MyContextManager:
    def __enter__(self):
        print('ENTER')

    def __exit__(self, cls_exception, exception, traceback):
        print('EXIT')

instancia = MyContextManager()

with instancia as inst:
    print('Executei o With')