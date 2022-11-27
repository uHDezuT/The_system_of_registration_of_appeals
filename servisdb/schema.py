import db_models


# Add File to DB
def add_appeal_to_db(db, **kwargs):
    new_appeal = db_models.Appeals(
        last_name=kwargs['last_name'],
        first_name=kwargs['first_name'],
        second_name=kwargs['second_name'],
        telephone=kwargs['telephone'],
        body=kwargs['body']
    )
    db.add(new_appeal)
    db.commit()
    db.refresh(new_appeal)
    return new_appeal


# Delete file from DB
def delete_file_from_db(db, file_info_from_db):
    db.delete(file_info_from_db)
    db.commit()
