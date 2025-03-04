class Checks:
    def position(self, int_obj, ext_obj):
        if int_obj.rect.left < ext_obj.left + int_obj.rect[2]:
            int_obj.rect.left = ext_obj.left+ int_obj.rect[2]
            return True

        if int_obj.rect.right > ext_obj.right - int_obj.rect[2]:
            int_obj.rect.right = ext_obj.right - int_obj.rect[2]
            return True

        if int_obj.rect.top < ext_obj.top + int_obj.rect[3]:
            int_obj.rect.top = ext_obj.top + int_obj.rect[3]
            return True

        if int_obj.rect.bottom > ext_obj.bottom - int_obj.rect[3]:
            int_obj.rect.bottom = ext_obj.bottom - int_obj.rect[3]
            return True
