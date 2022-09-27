CREATE TABLE "app_geeky_model_tutorial_fieldtypemodel" (
  "auto_field_example" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "boolean_field_exaple" bool NOT NULL, 
  "char_field_example" varchar(50) NOT NULL, 
  "date_field_exmaple" date NOT NULL, 
  "datetme_field_example" datetime NOT NULL, 
  "decimal_example" decimal NOT NULL, 
  "duration_exaple" bigint NOT NULL, 
  "email_example" varchar(254) NOT NULL, 
  "file_example" varchar(100) NOT NULL, 
  "file_path_example" varchar(100) NOT NULL, 
  "float_example" real NOT NULL, 
  "ip_exaple" real NOT NULL, 
  "imagne_exmaple" varchar(100) NOT NULL, 
  "integer_example" integer NOT NULL, 
  "json_example" text NOT NULL CHECK (
    (
      JSON_VALID("json_example") 
      OR "json_example" IS NULL
    )
  ), 
  "slug_example" varchar(50) NOT NULL, 
  "small_integer_exaple" smallint NOT NULL, 
  "txtfield_example" text NOT NULL, 
  "time_exaple" time NOT NULL, 
  "url_example" varchar(200) NOT NULL, 
  "uuid_eaxmple" char(32) NOT NULL
);
CREATE INDEX "app_geeky_model_tutorial_fieldtypemodel_slug_example_aeea5f09" ON "app_geeky_model_tutorial_fieldtypemodel" ("slug_example");
COMMIT;

CREATE TABLE "app_geeky_model_tutorial_entry" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "headline" varchar(255) NOT NULL, 
  "body_text" text NOT NULL, 
  "pub_date" date NOT NULL, 
  "mod_date" date NOT NULL, 
  "number_of_comments" integer NOT NULL, 
  "number_of_pingbacks" integer NOT NULL, 
  "rating" integer NOT NULL, 
  "blog_id" bigint NOT NULL REFERENCES "app_geeky_model_tutorial_blog" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE "app_geeky_model_tutorial_entry_authors" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "entry_id" bigint NOT NULL REFERENCES "app_geeky_model_tutorial_entry" ("id") DEFERRABLE INITIALLY DEFERRED, 
  "author_id" bigint NOT NULL REFERENCES "app_geeky_model_tutorial_author" ("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE INDEX "app_geeky_model_tutorial_entry_blog_id_310b7b0c" ON "app_geeky_model_tutorial_entry" ("blog_id");
CREATE UNIQUE INDEX "app_geeky_model_tutorial_entry_authors_entry_id_author_id_73cd9562_uniq" ON "app_geeky_model_tutorial_entry_authors" ("entry_id", "author_id");
CREATE INDEX "app_geeky_model_tutorial_entry_authors_entry_id_5a06c77c" ON "app_geeky_model_tutorial_entry_authors" ("entry_id");
CREATE INDEX "app_geeky_model_tutorial_entry_authors_author_id_99717877" ON "app_geeky_model_tutorial_entry_authors" ("author_id");
COMMIT;
