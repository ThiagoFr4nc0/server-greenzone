ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class communs():

    def _toJsonFromArray(arr):
        jsonData = []
        for m in arr:
            jsonData.append(m.toJson())
        return jsonData
    
    def _toJsonFromSimple(arr):
        jsonData = []
        for m in arr:
            jsonData.append(m.toJsonSimple())
        return jsonData

    def _allowed_file(filename):
        return '.' in filename and \
            filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS