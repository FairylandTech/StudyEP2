import wget


def downloads():

    data_url = 'https://github.com/Dreamacro/clash/releases/download/v1.10.6/clash-linux-amd64-v1.10.6.gz'
    data_path = r'D:\Downloads'
    http_proxy = '127.0.0.1:1080'
    wget.download(url=data_url, out=data_path)

    return True


if __name__ == '__main__':
    print(downloads())


