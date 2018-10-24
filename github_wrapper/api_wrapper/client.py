import gwrapper

class Client():

    def get_all_pulls():
        request = gwrapper.GWrapper("https://api.github.com/repos/oakbani/f3Github/pulls")
        request.list_pulls(state='created', sort='popularity')

    def get_pull(id):
        request = gwrapper.GWrapper("https://api.github.com/repos/oakbani/f3Github/pulls")
        request.list_pull(id)

    get_pull(1)
