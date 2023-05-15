-- Table: public.Crop_Seeding

-- DROP TABLE IF EXISTS public."Crop_Seeding";

CREATE TABLE IF NOT EXISTS public."Crop_Seeding"
(
    "Crop_Name" text COLLATE pg_catalog."default",
    "Seeding_Day" text COLLATE pg_catalog."default",
    id numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Crop_Seeding"
    OWNER to g4_user;




-- Table: public.Weather_Info

-- DROP TABLE IF EXISTS public."Weather_Info";

CREATE TABLE IF NOT EXISTS public."Weather_Info"
(
    "Day" text COLLATE pg_catalog."default",
    "Weather_Type" text COLLATE pg_catalog."default",
    id numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Weather_Info"
    OWNER to g4_user;



-- Table: public.Weather_Report

-- DROP TABLE IF EXISTS public."Weather_Report";

CREATE TABLE IF NOT EXISTS public."Weather_Report"
(
    "Reported_Weather_Type" text COLLATE pg_catalog."default",
    "Reporting_Time" timestamp without time zone,
    id numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Weather_Report"
    OWNER to g4_user;