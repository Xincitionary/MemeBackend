
USE `memedb` ;


-- drop schema if exists memedb;
-- create schema if not exists memedb;


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


INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName)
VALUES (NULL, 1, 2,2,3,1,"abtract 1", "topic 1");

INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName)
VALUES (NULL, 2, 3,12,32,1,"abtract 2", "topic 2");

INSERT INTO  api_topic(id, creator_id,num_followers,num_feeds,num_stories,trending, abstract, topicName)
VALUES (NULL, 3, 2,2,31,13,"abtract 1", "topic 3");


-- create posts
INSERT INTO  api_post(id, visibility, anonymous, view_count,create_time, topic_id,user_id,parent_id,is_story)
VALUES (NULL, 'visible', 1,1,CURRENT_TIMESTAMP, 1,1,NULL,1);

INSERT INTO  api_post(id, visibility, anonymous, view_count,create_time, topic_id,user_id,parent_id,is_story)
VALUES (NULL, 'invisible', 0,2,CURRENT_TIMESTAMP, 1,1,NULL,1);

INSERT INTO  api_post(id, visibility, anonymous, view_count,create_time, topic_id,user_id,parent_id,is_story)
VALUES (NULL, 'visible', 1,3,CURRENT_TIMESTAMP, 1,1,NULL,1);



-- p1 = Post(visibility = 'visible', anonymous =1, view_count = 2,create_time = datetime.now(), topic_id = 1, user_id = 1,parent_id = None, is_story = 1)