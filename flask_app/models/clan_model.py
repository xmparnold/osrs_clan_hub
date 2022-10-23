from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session


class Clan:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.motto = data[ 'motto' ]
        self.description = data[ 'description' ]
        self.logo_url = data[ 'logo_url' ]
        self.banner_url = data[ 'banner_url' ]
        self.privacy_level = data[ 'privacy_level' ]
        self.clan_creator_user_id = data[ 'clan_creator_user_id' ]

    @classmethod
    def get_one( cls, data ):
        pass

    @classmethod
    def get_all( cls ):
        pass
    
    @classmethod
    def create( cls, data ):
        pass

    @classmethod
    def get_one_with_creator( cls, data ):
        pass

    @classmethod
    def get_all_with_creators( cls, data ):
        pass

    @classmethod
    def get_one_with_events( cls, data ):
        pass
    
    @staticmethod
    def validate_clan_form( data ):
        pass

    