/*
 *  Types
 */
 CREATE TABLE IF NOT EXISTS iot_types(
   id INTEGER PRIMARY KEY AUTOINCREMENT,    -- id of type
   type VARCHAR(20) NOT NULL UNIQUE         -- IoT type
 );

CREATE TABLE IF NOT EXISTS sensor_types(
   id INTEGER PRIMARY KEY AUTOINCREMENT,    -- id of sensor
   type VARCHAR(20) NOT NULL UNIQUE         -- sensor type
 );

/*
 *  User tables
 */
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,           -- id of user
    user_login VARCHAR(30) NOT NULL UNIQUE,         -- user login
    user_pass VARCHAR(64) NOT NULL,                 -- user password
    user_nickname VARCHAR(30) NOT NULL,             -- user nickname
    user_email VARCHAR(50) NOT NULL UNIQUE,         -- email user
    user_registered DATETIME DEFAULT CURRENT_DATE   -- registered date
);

CREATE TABLE IF NOT EXISTS apikeys(
    id_user INTEGER NOT NULL,               -- id of user
    apikey VARCHAR(64) NOT NULL UNIQUE,     -- user apikey
    FOREIGN KEY (id_user)
        REFERENCES users(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS user_urls(
    id_user INTEGER NOT NULL,               -- id of user
    urls TEXT NOT NULL,                     -- user account urls
    FOREIGN KEY (id_user)
        REFERENCES users(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

/*
 *  Device tables
 */
CREATE TABLE IF NOT EXISTS user_devices(
    id_user INTEGER NOT NULL,               -- id of user
    d_id INTEGER PRIMARY KEY AUTOINCREMENT, -- user device id
    d_name VARCHAR(20) NOT NULL UNIQUE,     -- user device name
    d_mac VARCHAR(20) NOT NULL UNIQUE,      -- user device mac address
    FOREIGN KEY (id_user)
        REFERENCES users(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

/*
 *  IoT tables
 */
CREATE TABLE IF NOT EXISTS iots(
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- id of IoT
    name_iot VARCHAR(20) NOT NULL UNIQUE,   -- IoT name
    mac_iot VARCHAR(20) NOT NULL UNIQUE,    -- IoT mac address
    type_iot INTEGER NOT NULL,              -- IoT type
    FOREIGN KEY (type_iot)
        REFERENCES iot_types(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS sensors_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,               -- row id
    id_iot INTEGER NOT NULL,                            -- id of IoT
    type_data INTEGER NOT NULL,                         -- IoT type
    time_registration DATETIME DEFAULT CURRENT_DATE,    -- date + time
    sensor_data TEXT NOT NULL,                          -- sensor data
    FOREIGN KEY (id_iot)
        REFERENCES iots(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,
    FOREIGN KEY (type_data)
        REFERENCES sensor_types(id)
            ON DELETE CASCADE
            ON UPDATE CASCADE
);
