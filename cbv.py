from templator import render


class View:
    context = None
    template = None

    def __call__(self, request):
        out_template = render(self.template, object_list=[{'context': f'{self.context}'}])
        byte_out_template = bytes(out_template, 'utf-8')
        return '200 OK', byte_out_template

