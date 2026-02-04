--
-- PostgreSQL database cluster dump
--

\restrict 7IeH5HZeJzILMa8GTqqQgiitr1x4j71GsPDz9eIUtMaOEq2KpGFozhOyfBWnCrf

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;






\unrestrict 7IeH5HZeJzILMa8GTqqQgiitr1x4j71GsPDz9eIUtMaOEq2KpGFozhOyfBWnCrf

--
-- Databases
--

--
-- Database "template1" dump
--

\connect template1

--
-- PostgreSQL database dump
--

\restrict zkpocptgAyLEWlXKsEuyfldCZsxJhti4Aohvvt5h9dbj5OTLsAUr3OxYDjVoazh

-- Dumped from database version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)

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

--
-- PostgreSQL database dump complete
--

\unrestrict zkpocptgAyLEWlXKsEuyfldCZsxJhti4Aohvvt5h9dbj5OTLsAUr3OxYDjVoazh

--
-- Database "facultdb" dump
--

--
-- PostgreSQL database dump
--

\restrict Y6aD3H1YHl5rr9p42dk17Tl9eLzDv7zrird8dmyAquhUpcEOMtMMjpuE9guPY3x

-- Dumped from database version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)

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

--
-- Name: facultdb; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE facultdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE facultdb OWNER TO postgres;

\unrestrict Y6aD3H1YHl5rr9p42dk17Tl9eLzDv7zrird8dmyAquhUpcEOMtMMjpuE9guPY3x
\connect facultdb
\restrict Y6aD3H1YHl5rr9p42dk17Tl9eLzDv7zrird8dmyAquhUpcEOMtMMjpuE9guPY3x

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
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    id integer NOT NULL,
    name character varying(100),
    rank character varying(50),
    email character varying(100),
    phone character varying(20),
    office character varying(50),
    research_intrests text,
    remarks text
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- Name: faculty_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faculty_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faculty_id_seq OWNER TO postgres;

--
-- Name: faculty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faculty_id_seq OWNED BY public.faculty.id;


--
-- Name: faculty id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty ALTER COLUMN id SET DEFAULT nextval('public.faculty_id_seq'::regclass);


--
-- Data for Name: faculty; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty (id, name, rank, email, phone, office, research_intrests, remarks) FROM stdin;
\.


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_id_seq', 1, false);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict Y6aD3H1YHl5rr9p42dk17Tl9eLzDv7zrird8dmyAquhUpcEOMtMMjpuE9guPY3x

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

\restrict VUf5htMzBpcb2lNkexrhYsKnvnh3EE4Zc2RjHtluDvxGTIjBqSJXbi4jXsNKT90

-- Dumped from database version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.20 (Ubuntu 14.20-0ubuntu0.22.04.1)

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

--
-- PostgreSQL database dump complete
--

\unrestrict VUf5htMzBpcb2lNkexrhYsKnvnh3EE4Zc2RjHtluDvxGTIjBqSJXbi4jXsNKT90

--
-- PostgreSQL database cluster dump complete
--

