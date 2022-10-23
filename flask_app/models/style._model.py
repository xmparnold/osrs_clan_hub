from cgitb import reset
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session

class Style:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.bg_color = data[ 'background_color' ]
        self.font_color = data[ 'font_color' ]
        self.font_type = data[ 'font_type' ]
        self.title_font_color = data[ 'title_font_color' ]
        self.font_size = data[ 'font_size' ]
        self.title_font_size = data[ 'title_font_size' ]
        self.border_thickness = data[ 'border_thickness' ]
        self.border_color = data[ 'border_color' ]
        self.border_style = data[ 'border_style' ]
        self.content_box_bg_color = data[ 'content_box_bg_color']
        self.accent_color_1 = data[ 'accent_color_1' ]
        self.accent_color_2 = data[ 'accent_color_2' ]
        self.accent_color_3 = data[ 'accent_color_3' ]
        self.clan_id = data[ 'clan_id' ]
        self.creator_user_id = data[ 'creator_user_id' ]
        
    @classmethod
    def get_one( cls, data ):
        query = "SELECT * FROM styles WHERE id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0:
            style = cls( result[ 0 ] )
            return style
        else:
            return None

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM styles;"
        result = connectToMySQL( DATABASE ).query_db( query )

        list_styles = []

        if len( result ) > 0:
            for row in result:
                current_style = cls( row )
                list_styles.append( current_style )
        
        return list_styles


    @classmethod
    def get_all_by_clan_id( cls, data ):
        query = "SELECT * FROM styles WHERE clan_id = %(clan_id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        list_styles = []

        if len( result ) > 0:
            for row in result:
                current_style = cls( row )
                list_styles.append( current_style )
        
        return list_styles

    @classmethod
    def create( cls, data ):
        pass

    @classmethod
    def delete( cls, data ):
        query = "DELETE FROM styles WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    classmethod
    def edit( cls, data ):
        pass
