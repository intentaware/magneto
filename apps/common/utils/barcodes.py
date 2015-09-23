from django.conf import settings

from reportlab.lib.units import mm
from reportlab.graphics.barcode import createBarcodeDrawing
from reportlab.graphics.shapes import Drawing, String

class BarcodeFromString(Drawing):
    def __init__(self, text, *args, **kwargs):
        barcode = createBarcodeDrawing(
            'Code128', value=text, barHeight=10*mm, humanReadable=True)
        Drawing.__init__(
            self, barcode.width,barcode.height,*args,**kwargs)
        self.add(barcode, text)
        from django.core.files.storage import default_storage
        outDir = default_storage.path('coupons')
        try:
            default_storage.path('coupons')
        except NotImplementedError:
            default_storage.location(
                '%s/%s' %(settings.MEDIAFILES_LOCATION, 'coupons'))
        self.save(
                formats = ['png',],
                outDir = outDir,
                fnRoot=text,
            )
