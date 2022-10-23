from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session

class Event:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.description = data[ 'description' ]
        self.location = data[ 'location' ]
        self.scheduled_date = data[ 'scheduled_date' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]
        self.clan_id = data[ 'clan_id' ]
        self.requirements = data[ 'requirements' ]
        self.creator_user_id = data[ 'creator_user_id' ]
        
    @classmethod
    def get_one( cls, data ):
        query = "SELECT * FROM events WHERE id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0:
            event = cls( result[ 0 ] )
            return event
        else:
            return None

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM events;"
        result = connectToMySQL( DATABASE ).query_db( query )

        list_events = []

        if len( result ) > 0:
            for row in result:
                current_event = cls( row )
                list_events.append( current_event )
        
        return list_events


    @classmethod
    def get_all_by_clan( cls, data ):
        query = "SELECT * FROM events WHERE clan_id = %(clan_id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        list_events = []

        if len( result ) > 0:
            for row in result:
                current_event = cls( row )
                list_events.append( current_event )

        return list_events

    @classmethod
    def get_all_by_creator( cls, data ):
        query = "SELECT * FROM events WHERE creator_user_id = %(user_id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        list_events = []

        if len( result ) > 0:
            query = "SELECT * FROM events WHERE"

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO events (name, description, scheduled_date, clan_id, location, requirements, creator_user_id) VALUES(%(name)s, %(description)s, %(scheduled_date)s, %(clan_id)s, %(location)s, %(requirements)s, %(creator_user_id)s);"
        id_new_event = connectToMySQL( DATABASE ).query_db( query, data )
        return id_new_event

    @classmethod
    def delete( cls, data ):
        # first we delete all the rsvp entries for given event to avoid errors and unneeded info in this table
        query = "DELETE FROM rsvp WHERE event_id = %(id)s;"
        connectToMySQL( DATABASE ).query_db( query, data )

        # now we can delete the event from the db
        query = "DELETE FROM events WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )


    @classmethod
    def edit( cls, data ):
        query = "UPDATE events SET name = %(name)s, description = %(description)s, scheduled_date = %(scheduled_date)s, clan_id = %(clan_id)s, location = %(location)s, requirements = %(requirements)s, creator_user_id = %(the,)s WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def rsvp( cls, data ):
        query = "INSERT INTO rsvp (event_id, user_id) VALUES(%(event_id)s, %(user_id)s);"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def undo_rsvp( cls, data ):
        query = "DELETE FROM rsvp WHERE event_id = %(event_id)s AND user_id = %(user_id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

        











