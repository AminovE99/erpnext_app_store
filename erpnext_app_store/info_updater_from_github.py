import json

import frappe
import requests
from erpnext_app_store.erpnext_app_store.doctype.application.application import Application


def update_info():
    raw_info = requests.get('https://raw.githubusercontent.com/Monogramm/erpnext_app_listing/master/apps.csv')
    list_of_repo = raw_info.text.split('\n')
    list_of_repo.pop()
    for repo_link in list_of_repo:
        value = repo_link.split('https://github.com/')[1]
        user_name, title = value.split('/')
        info = requests.get("https://api.github.com/repos/{}/{}".format(user_name, title))
        json_dict = json.loads(info.text)
        #need to add the checker
        app = Application({
            'doctype': 'Application',
            'title': title,#fix it
            'description': json_dict.get('description'),
            'link_to_github': repo_link
        }
        )
        app.save()
    # else:
    #     app_from_db.doctype = Application
    #     app_from_db.title = json_dict['name']
    #     app_from_db.description = json_dict['description']
    #     app_from_db.link_to_github = repo_link
    #     app_from_db.save()


if __name__ == '__main__':
    update_info()
