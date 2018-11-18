"""
Dylan Bossie

When a user uploads an image through the HTML UI, the image metadata must be
stored to the Heroku database under the associated user's account.
"""

def addImageData(conn,cur,username,userid):
    foldername = "TestFolder"
    imagename = "TestImage"
    description = "https://s3-us-west-2.amazonaws.com/" + \
    foldername + "/" + imagename + ".jpg"
    active = "True"
    cur.execute("insert into pictures (userrolename,userid,descripion,active) values (%s,%s,%s,%s);",
                (username,userid,description,active))
    conn.commit()
    
    return