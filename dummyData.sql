
USE `memedb` ;


-- drop schema if exists memedb;
-- create schema if not exists memedb;

-- ALTER TABLE api_topic AUTO_INCREMENT=1;
-- DELETE FROM TABLE WHERE xxx;

-- Create userlogins 
-- DELETE FROM api_userlogin WHERE id <10;
-- ALTER TABLE api_userlogin AUTO_INCREMENT = 1;
INSERT INTO api_userlogin(id, username, password,create_time) VALUES
(NULL, 'u1', 'user1',CURRENT_TIMESTAMP);

INSERT INTO api_userlogin(id, username, password,create_time) VALUES
(NULL, 'u2', 'user2',CURRENT_TIMESTAMP);

INSERT INTO api_userlogin(id, username, password,create_time) VALUES
(NULL, 'u3', 'user3',CURRENT_TIMESTAMP);



-- Create topics



INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName,create_time, last_updated)
VALUES (NULL, 1, 2,2,3,1,"abtract 1", "topic 1", CURRENT_TIMESTAMP,CURRENT_TIMESTAMP );

INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName,create_time, last_updated)
VALUES (NULL, 2, 3,12,32,1,"abtract 2", "topic 2", CURRENT_TIMESTAMP,CURRENT_TIMESTAMP );

INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName,create_time, last_updated)
VALUES (NULL, 3, 2,2,31,13,"abtract 1", "topic 3", CURRENT_TIMESTAMP,CURRENT_TIMESTAMP );




-- create stories
INSERT INTO  api_story(id, visibility, anonymous, view_count,create_time, title, content, parent_id, topic_id,user_id)
VALUES (NULL, 'visible', 1,1,CURRENT_TIMESTAMP, 'story1', 'some content', NULL,3,1);


-- p1 = Post(visibility = 'visible', anonymous =1, view_count = 2,create_time = datetime.now(), topic_id = 1, user_id = 1,parent_id = None, is_story = 1)