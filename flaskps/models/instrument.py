class Instrument(object):

    db = None

    @classmethod
    def all(cls):
        cursor = cls.db.cursor()
        sql = """
            SELECT instruments.instrument_id, instruments.name, instruments.code, instrument_types.name AS type FROM instruments
            INNER JOIN instrument_types ON instruments.instrument_type_id = instrument_types.instrument_type_id
        """
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def get(cls, instrument_id):
        cursor = cls.db.cursor()
        sql = """
            SELECT instruments.instrument_id, instruments.name, instruments.code, instruments.instrument_type_id, instrument_types.name AS type FROM instruments
            INNER JOIN instrument_types ON instruments.instrument_type_id = instrument_types.instrument_type_id
            WHERE instruments.instrument_id=%s
        """
        cursor.execute(sql, (instrument_id))
        return cursor.fetchone()

    @classmethod
    def get_image(cls, instrument_id):
        cursor = cls.db.cursor()
        sql = "SELECT instruments.image FROM instruments WHERE instruments.instrument_id=%s"
        cursor.execute(sql, (instrument_id))
        return cursor.fetchone()

    @classmethod
    def create(cls, instrument, file):
        cursor = cls.db.cursor()
        sql = """
            INSERT INTO instruments (name, code, instrument_type_id, image) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (instrument['name'], instrument['code'], instrument['instrument_type_id'], file))
        cls.db.commit()
        return True

    @classmethod
    def update(cls, instrument):
        #img = request['img']
        cursor = cls.db.cursor()
        sql= "UPDATE instruments SET name=%s, code=%s, instrument_type_id=%s WHERE instrument_id=%s"
        cursor.execute(sql, (instrument['name'], instrument['code'], instrument['instrument_type_id'], instrument['instrument_id']))
        cls.db.commit()
        return True

    @classmethod
    def update_with_image(cls, instrument, image):
        #img = request['img']
        cursor = cls.db.cursor()
        sql= "UPDATE instruments SET name=%s, code=%s, instrument_type_id=%s, image=%s WHERE instrument_id=%s"
        cursor.execute(sql, (instrument['name'], instrument['code'], instrument['instrument_type_id'], image, instrument['instrument_id']))
        cls.db.commit()
        return True

    @classmethod
    def delete(cls, instrument_id):
        cursor = cls.db.cursor()
        cursor.execute("DELETE FROM instruments WHERE instrument_id=%s", (instrument_id))
        cls.db.commit()
        return True
