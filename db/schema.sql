DROP TABLE IF EXISTS colors;
DROP TABLE IF EXISTS modes;
DROP TABLE IF EXISTS fonts;
DROP TABLE IF EXISTS messages;

CREATE TABLE colors (
	  color_id INTEGER PRIMARY KEY autoincrement,
	    color_name TEXT NOT NULL
);

CREATE TABLE modes (
	    mode_id INTEGER PRIMARY KEY autoincrement,
	  mode_name TEXT NOT NULL
);

CREATE TABLE fonts (
	    font_id INTEGER PRIMARY KEY autoincrement,
	    font_name TEXT NOT NULL
);

CREATE TABLE messages (
	  message_id INTEGER PRIMARY KEY autoincrement,
	  text TEXT NOT NULL,
	  color_id INTEGER DEFAULT 1,
	  mode_id INTEGER DEFAULT 1,
	  font_id INTEGER DEFAULT 1,
	  FOREIGN KEY (color_id) REFERENCES colors (color_id) ON DELETE SET DEFAULT,
	  FOREIGN KEY (mode_id) REFERENCES modes (mode_id) ON DELETE SET DEFAULT,
	  FOREIGN KEY (font_id) REFERENCES fonts (font_id) ON DELETE SET DEFAULT
);

INSERT INTO colors (color_name) VALUES ("RED");
INSERT INTO colors (color_name) VALUES ("AUTOCOLOR");
INSERT INTO colors (color_name) VALUES ("GREEN");
INSERT INTO colors (color_name) VALUES ("AMBER");
INSERT INTO colors (color_name) VALUES ("RAINBOW_1");
INSERT INTO colors (color_name) VALUES ("RAINBOW_2");
INSERT INTO colors (color_name) VALUES ("COLOR_MIX");

INSERT INTO modes (mode_name) VALUES ("ROTATE");
INSERT INTO modes (mode_name) VALUES ("HOLD");
INSERT INTO modes (mode_name) VALUES ("ROLL_UP");
INSERT INTO modes (mode_name) VALUES ("ROLL_DOWN");
INSERT INTO modes (mode_name) VALUES ("ROLL_LEFT");
INSERT INTO modes (mode_name) VALUES ("ROLL_RIGHT");
INSERT INTO modes (mode_name) VALUES ("WIPE_UP");
INSERT INTO modes (mode_name) VALUES ("WIPE_DOWN");
INSERT INTO modes (mode_name) VALUES ("WIPE_LEFT");
INSERT INTO modes (mode_name) VALUES ("WIPE_RIGHT");
INSERT INTO modes (mode_name) VALUES ("SCROLL");
INSERT INTO modes (mode_name) VALUES ("ROLL_IN");
INSERT INTO modes (mode_name) VALUES ("ROLL_OUT");
INSERT INTO modes (mode_name) VALUES ("WIPE_IN");
INSERT INTO modes (mode_name) VALUES ("WIPE_OUT");
INSERT INTO modes (mode_name) VALUES ("TWINKLE");
INSERT INTO modes (mode_name) VALUES ("SPARKLE");
INSERT INTO modes (mode_name) VALUES ("SNOW");
INSERT INTO modes (mode_name) VALUES ("INTERLOCK");
INSERT INTO modes (mode_name) VALUES ("SWITCH");
INSERT INTO modes (mode_name) VALUES ("SPRAY");
INSERT INTO modes (mode_name) VALUES ("STARBURST");
INSERT INTO modes (mode_name) VALUES ("WELCOME");
INSERT INTO modes (mode_name) VALUES ("SLOT_MACHINE");
INSERT INTO modes (mode_name) VALUES ("THANK_YOU");
INSERT INTO modes (mode_name) VALUES ("NO_SMOKING");
INSERT INTO modes (mode_name) VALUES ("DONT_DRINK_DRIVE");
INSERT INTO modes (mode_name) VALUES ("RUNNING_ANIMAL");
INSERT INTO modes (mode_name) VALUES ("FIREWORKS");
INSERT INTO modes (mode_name) VALUES ("TURBO_CAR");

INSERT INTO fonts (font_name) VALUES ("FIVE_HIGH_STD");
INSERT INTO fonts (font_name) VALUES ("SEVEN_HIGH_STD");
INSERT INTO fonts (font_name) VALUES ("SEVEN_HIGH_FANCY");
