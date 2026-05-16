-- I will create someone
CREATE USER IF NOT EXISTS user_0d_1;
IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT
ON *.*
TO user_0d_1;
