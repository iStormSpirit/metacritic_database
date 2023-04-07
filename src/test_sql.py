# -- INSERT INTO game (id, name, game_publisher_id) VALUES (1, 'batman', 1);
# -- INSERT INTO game SET (id, name, game_publisher_id) VALUES (1, 'batman2', 1);
# -- UPDATE game SET game_publisher_id=1 WHERE id=1
#
# -- UPDATE game SET name='batman3', game_publisher_id=1 WHERE id=1
# -- INSERT INTO publisher (id, name) VALUES (3, 'qwe')
#
# -- INSERT INTO game (id, name, game_publisher_id) VALUES (6, 'zz', 2);
#
# -- SELECT id, name FROM game WHERE game_publisher_id=2
#
#
# -- SELECT id, name as pub_id FROM publisher WHERE publisher.id=1
# -- SELECT game.id, game.name FROM game, publisher WHERE game.game_publisher_id=2
# -- SELECT id as pub_id FROM publisher WHERE name='WB';
# -- SELECT game.id, game.name FROM game WHERE game_publisher_id=INT(pub_id);
#
# SELECT game.id, game.name FROM game WHERE game_publisher_id=(SELECT id FROM publisher WHERE name='WB')