--
-- PostgreSQL database dump
--

-- Dumped from database version 14.12 (Debian 14.12-1.pgdg120+1)
-- Dumped by pg_dump version 14.12 (Debian 14.12-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS hakunamatata;
--
-- Name: hakunamatata; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE hakunamatata WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'C.UTF-8';


ALTER DATABASE hakunamatata OWNER TO postgres;

\connect hakunamatata

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: scale_data; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.scale_data (
    weight numeric,
    bmi numeric,
    height numeric,
    insert_date timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    body_fat_percentage numeric,
    basal_metabolism numeric,
    muscle_percentage numeric,
    soft_lean_mass numeric,
    body_water_mass numeric,
    impedance numeric
);


ALTER TABLE public.scale_data OWNER TO postgres;

--
-- PostgreSQL database dump complete
--

