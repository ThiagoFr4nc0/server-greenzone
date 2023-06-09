ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class communs():

    def _toJsonFromData(data):
        jsonData = []
        for m in data:
            jsonData.append(m.toJson())
        return jsonData

    def _allowed_file(filename):
        return '.' in filename and \
            filename.split('.')[-1].lower() in ALLOWED_EXTENSIONS