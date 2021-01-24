/*
 *  Types
 */
 CREATE TABLE iot_types(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   type VARCHAR(20) NOT NULL
 );

CREATE TABLE sensor_types(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   type VARCHAR(20) NOT NULL
 );

/*
 *  User tables
 */
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- id of user
    user_login VARCHAR(30) NOT NULL,        -- user login
    user_pass VARCHAR(64) NOT NULL,         -- user password
    user_nickname VARCHAR(30) NOT NULL,     -- user nicname
    user_email VARCHAR(50) NOT NULL,        -- email user
    user_registered DATETIME NOT NULL       -- registered date
);

CREATE TABLE apikeys(
    id_user INTEGER NOT NULL,               -- id of user
    apikey VARCHAR(64) UNIQUE NOT NULL,     -- user apikey
    FOREIGN KEY (id_user) REFERENCES users(id)
);

CREATE TABLE user_urls(
    id_user INTEGER NOT NULL,               -- id of user
    urls TEXT NOT NULL,                     -- user account urls
    FOREIGN KEY (id_user) REFERENCES users(id)
);

/*
 *  Device tables
 */
CREATE TABLE user_devices(
    id_user INTEGER NOT NULL,               -- id of user
    d_id INTEGER PRIMARY KEY AUTOINCREMENT, -- user device id
    d_name VARCHAR(20) NOT NULL,            -- user device name
    d_mac VARCHAR(20) NOT NULL              -- user device mac address
);

/*
 *  IoT tables
 */
CREATE TABLE iots(
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- id of IoT
    name_iot VARCHAR(20) NOT NULL,          -- IoT name
    mac_iot VARCHAR(20) NOT NULL,           -- IoT mac address
    type_iot INTEGER NOT NULL,              -- IoT type
    FOREIGN KEY (type_iot) REFERENCES iot_types(id)
);

CREATE TABLE sensors_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_iot INTEGER NOT NULL,
    type_data INTEGER NOT NULL,
    time_registration DATETIME NOT NULL,
    sensor_data TEXT NOT NULL,
    FOREIGN KEY (id_iot) REFERENCES iots(id),
    FOREIGN KEY (type_data) REFERENCES sensor_types(id)
);
