import vk_api

from vk_api.utils import get_random_id


vk_session = vk_api.VkApi('login', 'password', app_id=2685278)
vk_session.auth()
vk = vk_session.get_api()


def sendAudioMessage(vk: vk_api, file: str, link: str) -> int:
    """
    1
        vk_session = vk_api.VkApi('login', 'password', app_id=2685278)
        vk_session.auth()
        vk = vk_session.get_api()

    2 путь к файлу

    3
        Для пользователя:
            id пользователя.

            Для групповой беседы:
            (2000000000: int + id: int) беседы. id беседы для каждого пользователя уникально из-за особенности вк

            Для сообщества:
            -id сообщества.

    :return: id сообщения
    """
    json = vk_api.upload.VkUpload(vk).audio_message(r'{0}'.format(file), id)
    message = vk.messages.send(peer_id=id,
                    attachment='audio_message{0}_{1}>'.format(str(json['audio_message']['owner_id']),
                                                              str(json['audio_message']['id'])),
                    random_id=get_random_id())
    return message


def sendVideoMessage(vk: vk_api, file: str, id: str) -> int:
    """
    смотри доку sendAudioMessage
    """
    json = vk_api.upload.VkUpload(vk).video(r'{0}'.format(file), name='123')
    message = vk.messages.send(peer_id=id,
                     attachment='video{0}_{1}>'.format(str(json['owner_id']),
                                                       str(json['video_id'])),
                     random_id=get_random_id())
    return message


def sendDocMessage(vk: vk_api, file: str, id: str) -> int:
    """
    смотри доку sendAudioMessage
    """
    json = vk_api.upload.VkUpload(vk).document_message(r'{0}'.format(file), id)
    message = vk.messages.send(peer_id=id,
                     attachment='doc{0}_{1}>'.format(str(json['doc']['owner_id']),
                                                     str(json['doc']['id'])),
                     random_id=get_random_id())
    return message


def sendGraffitiMessage(vk: vk_api, file: str, id: str) -> int:
    """
    смотри доку sendAudioMessage
    """
    json = vk_api.upload.VkUpload(vk).graffiti(r'{0}'.format(file), id)
    message = vk.messages.send(peer_id=id,
                     attachment='graffiti{0}_{1}>'.format(str(json['graffiti']['owner_id']),
                                                          str(json['graffiti']['id'])),
                     random_id=get_random_id())
    return message


def sendPhotoMessage(vk: vk_api, file: str, id: str) -> int:
    """
    смотри доку sendAudioMessage
    """
    json = vk_api.upload.VkUpload(vk).photo_messages(r'{0}'.format(file), id)
    message = vk.messages.send(peer_id=id,
                     attachment='photo{0}_{1}>'.format(str(json[0]['owner_id']),
                                                       str(json[0]['id'])),
                     random_id=get_random_id())
    return message


def getFriends(vk: vk_api) -> dict:
    """
    vk_session = vk_api.VkApi('login', 'password', app_id=2685278)
    vk_session.auth()
    vk = vk_session.get_api()

    Получаем массив друзей
    :param vk: vk_api
    """
    friends = vk.friends.get(fields=['contacts', 'name', 'sex'])
    return friends


def getChats(vk: vk_api):
    """
    vk_session = vk_api.VkApi('login', 'password', app_id=2685278)
    vk_session.auth()
    vk = vk_session.get_api()

    Получаем массив последних 20 диалогов
    :param vk: vk_api
    """
    chats = vk.messages.getConversations()
    for i in chats['items']:
        print(i['conversation'])
        print(i['conversation']['peer']['id'])
        if i['conversation']['peer']['type'] == 'user':
            print('user')
        elif i['conversation']['peer']['type'] == 'group':
            print('group')
        elif i['conversation']['peer']['type'] == 'chat':
            print(i['conversation']['chat_settings']['title'])
    return chats