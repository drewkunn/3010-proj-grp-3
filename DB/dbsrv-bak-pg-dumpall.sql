--
-- PostgreSQL database cluster dump
--

\restrict BqX1e4fDMNb8Romax7wjLJOG9XJEWVxx6NzaaehIaXCbDBqP2kzMb4IPzVa3p8k

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS;
CREATE ROLE webuser1;
ALTER ROLE webuser1 WITH NOSUPERUSER INHERIT NOCREATEROLE NOCREATEDB LOGIN NOREPLICATION NOBYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:Oy79n8u5fV294taIEvu9JA==$Zva7n0Wil4MQlfHbtjwJT4feGvAWcYPw4Ln+k0sDJCA=:jW+ey/zp1XsymzkR7k+VpbW0dcpN9TlB4jzl42erp7Q=';






\unrestrict BqX1e4fDMNb8Romax7wjLJOG9XJEWVxx6NzaaehIaXCbDBqP2kzMb4IPzVa3p8k

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

\restrict fCWQVT0SxnUP3wsxaV8NTtf7x1rePKYKYjbrJtTRdjQeWiealbA6FsSvhjGsz3z

-- Dumped from database version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)

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

\unrestrict fCWQVT0SxnUP3wsxaV8NTtf7x1rePKYKYjbrJtTRdjQeWiealbA6FsSvhjGsz3z

--
-- Database "dashboard" dump
--

--
-- PostgreSQL database dump
--

\restrict 7vdt9qXzaNC1uPHgOVyAConba4PEAdwTlrcXdsJbX3QmDpB5LytdLqgO52xgtbg

-- Dumped from database version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)

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
-- Name: dashboard; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE dashboard WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE dashboard OWNER TO postgres;

\unrestrict 7vdt9qXzaNC1uPHgOVyAConba4PEAdwTlrcXdsJbX3QmDpB5LytdLqgO52xgtbg
\connect dashboard
\restrict 7vdt9qXzaNC1uPHgOVyAConba4PEAdwTlrcXdsJbX3QmDpB5LytdLqgO52xgtbg

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
    name text,
    department text,
    email text
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

COPY public.faculty (id, name, department, email) FROM stdin;
1	John Smith	Computer Science	smith@ecu.edu
2	Jane Doe	Mathematics	doe@ecu.edu
\.


--
-- Name: faculty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_id_seq', 2, true);


--
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);


--
-- Name: DATABASE dashboard; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON DATABASE dashboard TO webuser1;


--
-- Name: TABLE faculty; Type: ACL; Schema: public; Owner: postgres
--

GRANT ALL ON TABLE public.faculty TO webuser1;


--
-- PostgreSQL database dump complete
--

\unrestrict 7vdt9qXzaNC1uPHgOVyAConba4PEAdwTlrcXdsJbX3QmDpB5LytdLqgO52xgtbg

--
-- Database "facultdb" dump
--

--
-- PostgreSQL database dump
--

\restrict I7chpXCB8SGHaPwD1Mfff3gdmfWo9bDAUZ3Gn34GzuUdYSD5aGDVGEPsu6RqvhD

-- Dumped from database version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)

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

\unrestrict I7chpXCB8SGHaPwD1Mfff3gdmfWo9bDAUZ3Gn34GzuUdYSD5aGDVGEPsu6RqvhD
\connect facultdb
\restrict I7chpXCB8SGHaPwD1Mfff3gdmfWo9bDAUZ3Gn34GzuUdYSD5aGDVGEPsu6RqvhD

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

\unrestrict I7chpXCB8SGHaPwD1Mfff3gdmfWo9bDAUZ3Gn34GzuUdYSD5aGDVGEPsu6RqvhD

--
-- Database "postgres" dump
--

\connect postgres

--
-- PostgreSQL database dump
--

\restrict D1fMu9W9XSGpSkHrNTNI13CfFaVhbeLUd9IBTwJlQ2Wj3EQVdcDtP0NlTDlZvfh

-- Dumped from database version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.22 (Ubuntu 14.22-0ubuntu0.22.04.1)

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
-- Name: faculty_committees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty_committees (
    id integer NOT NULL,
    committee_name character varying(50),
    faculty_name character varying(50),
    role character varying(20)
);


ALTER TABLE public.faculty_committees OWNER TO postgres;

--
-- Name: faculty_committees_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.faculty_committees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.faculty_committees_id_seq OWNER TO postgres;

--
-- Name: faculty_committees_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.faculty_committees_id_seq OWNED BY public.faculty_committees.id;


--
-- Name: recources; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recources (
    id integer NOT NULL,
    resource_name character varying(50),
    category character varying(30),
    location character varying(30)
);


ALTER TABLE public.recources OWNER TO postgres;

--
-- Name: recources_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recources_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recources_id_seq OWNER TO postgres;

--
-- Name: recources_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recources_id_seq OWNED BY public.recources.id;


--
-- Name: faculty_committees id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty_committees ALTER COLUMN id SET DEFAULT nextval('public.faculty_committees_id_seq'::regclass);


--
-- Name: recources id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recources ALTER COLUMN id SET DEFAULT nextval('public.recources_id_seq'::regclass);


--
-- Data for Name: faculty_committees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.faculty_committees (id, committee_name, faculty_name, role) FROM stdin;
\.


--
-- Data for Name: recources; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recources (id, resource_name, category, location) FROM stdin;
\.


--
-- Name: faculty_committees_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.faculty_committees_id_seq', 1, false);


--
-- Name: recources_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recources_id_seq', 1, false);


--
-- Name: faculty_committees faculty_committees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty_committees
    ADD CONSTRAINT faculty_committees_pkey PRIMARY KEY (id);


--
-- Name: recources recources_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recources
    ADD CONSTRAINT recources_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict D1fMu9W9XSGpSkHrNTNI13CfFaVhbeLUd9IBTwJlQ2Wj3EQVdcDtP0NlTDlZvfh

--
-- PostgreSQL database cluster dump complete
--

