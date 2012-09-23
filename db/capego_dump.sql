--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: capego; Type: DATABASE; Schema: -; Owner: adrian
--

CREATE DATABASE capego WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_AU.UTF-8' LC_CTYPE = 'en_AU.UTF-8';


ALTER DATABASE capego OWNER TO adrian;

\connect capego

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO adrian;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO adrian;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO adrian;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO adrian;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO adrian;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO adrian;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_permission_id_seq', 30, true);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    is_superuser boolean NOT NULL,
    last_login timestamp with time zone NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO adrian;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO adrian;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO adrian;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO adrian;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO adrian;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO adrian;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    content_type_id integer,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO adrian;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO adrian;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 18, true);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO adrian;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO adrian;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('django_content_type_id_seq', 10, true);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO adrian;

--
-- Name: django_site; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.django_site OWNER TO adrian;

--
-- Name: django_site_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE django_site_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_site_id_seq OWNER TO adrian;

--
-- Name: django_site_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE django_site_id_seq OWNED BY django_site.id;


--
-- Name: django_site_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('django_site_id_seq', 1, true);


--
-- Name: listener_accent; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE listener_accent (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    language_id integer NOT NULL
);


ALTER TABLE public.listener_accent OWNER TO adrian;

--
-- Name: listener_accent_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE listener_accent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listener_accent_id_seq OWNER TO adrian;

--
-- Name: listener_accent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE listener_accent_id_seq OWNED BY listener_accent.id;


--
-- Name: listener_accent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('listener_accent_id_seq', 1, false);


--
-- Name: listener_language; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE listener_language (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.listener_language OWNER TO adrian;

--
-- Name: listener_language_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE listener_language_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listener_language_id_seq OWNER TO adrian;

--
-- Name: listener_language_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE listener_language_id_seq OWNED BY listener_language.id;


--
-- Name: listener_language_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('listener_language_id_seq', 3, true);


--
-- Name: listener_listener; Type: TABLE; Schema: public; Owner: adrian; Tablespace: 
--

CREATE TABLE listener_listener (
    id integer NOT NULL,
    url character varying(500) NOT NULL,
    title character varying(200) NOT NULL,
    description text NOT NULL,
    pub_date timestamp with time zone NOT NULL,
    update_date timestamp with time zone NOT NULL,
    broken boolean NOT NULL,
    language_id integer NOT NULL,
    length smallint
);


ALTER TABLE public.listener_listener OWNER TO adrian;

--
-- Name: listener_listener_id_seq; Type: SEQUENCE; Schema: public; Owner: adrian
--

CREATE SEQUENCE listener_listener_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.listener_listener_id_seq OWNER TO adrian;

--
-- Name: listener_listener_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: adrian
--

ALTER SEQUENCE listener_listener_id_seq OWNED BY listener_listener.id;


--
-- Name: listener_listener_id_seq; Type: SEQUENCE SET; Schema: public; Owner: adrian
--

SELECT pg_catalog.setval('listener_listener_id_seq', 5, true);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY django_site ALTER COLUMN id SET DEFAULT nextval('django_site_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY listener_accent ALTER COLUMN id SET DEFAULT nextval('listener_accent_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY listener_language ALTER COLUMN id SET DEFAULT nextval('listener_language_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY listener_listener ALTER COLUMN id SET DEFAULT nextval('listener_listener_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add permission	1	add_permission
2	Can change permission	1	change_permission
3	Can delete permission	1	delete_permission
4	Can add group	2	add_group
5	Can change group	2	change_group
6	Can delete group	2	delete_group
7	Can add user	3	add_user
8	Can change user	3	change_user
9	Can delete user	3	delete_user
10	Can add content type	4	add_contenttype
11	Can change content type	4	change_contenttype
12	Can delete content type	4	delete_contenttype
13	Can add session	5	add_session
14	Can change session	5	change_session
15	Can delete session	5	delete_session
16	Can add site	6	add_site
17	Can change site	6	change_site
18	Can delete site	6	delete_site
19	Can add log entry	7	add_logentry
20	Can change log entry	7	change_logentry
21	Can delete log entry	7	delete_logentry
22	Can add language	8	add_language
23	Can change language	8	change_language
24	Can delete language	8	delete_language
25	Can add listener	9	add_listener
26	Can change listener	9	change_listener
27	Can delete listener	9	delete_listener
28	Can add accent	10	add_accent
29	Can change accent	10	change_accent
30	Can delete accent	10	delete_accent
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_user (id, username, first_name, last_name, email, password, is_staff, is_active, is_superuser, last_login, date_joined) FROM stdin;
1	adrian			deccico@gmail.com	pbkdf2_sha256$10000$NOSY3McPqwEs$1rvGHMlRnHXiN1yoLHBtwm6mjnuU5b8Ul3itcx0HgZI=	t	t	t	2012-09-23 14:32:40.892715+10	2012-09-23 14:31:55.108615+10
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY django_admin_log (id, action_time, user_id, content_type_id, object_id, object_repr, action_flag, change_message) FROM stdin;
1	2012-09-23 14:32:52.181857+10	1	8	1	English	1	
2	2012-09-23 14:33:06.582049+10	1	8	2	Español	1	
3	2012-09-23 14:33:16.841826+10	1	8	3	Italiano	1	
4	2012-09-23 14:55:15.426744+10	1	8	1	English	1	
5	2012-09-23 14:55:19.608706+10	1	8	2	Italiano	1	
6	2012-09-23 14:55:27.752116+10	1	8	3	Español	1	
7	2012-09-23 14:58:13.427985+10	1	8	1	English	1	
8	2012-09-23 14:58:19.137999+10	1	8	2	Español	1	
9	2012-09-23 14:58:24.608474+10	1	8	3	Italiano	1	
10	2012-09-23 15:35:59.569976+10	1	9	3	English-Homer lie detector-http://www.youtube.com/watch?v=HqmHXnryakA	1	
11	2012-09-23 20:01:41.892871+10	1	9	4	English-South Park Parody of iPad Ad-http://vimeo.com/15243319	1	
12	2012-09-23 20:02:01.793749+10	1	9	4	English-South Park Parody of iPad Ad-http://vimeo.com/15243319	2	Changed length.
13	2012-09-23 20:02:43.202524+10	1	9	3	English-Homer lie detector-http://www.youtube.com/watch?v=HqmHXnryakA	2	Changed length.
14	2012-09-23 20:08:58.256274+10	1	9	5	English-Simpsons - South Park parody-http://vimeo.com/8221814	1	
15	2012-09-23 20:26:15.580372+10	1	9	4	English-South Park Parody of iPad Ad-<iframe src="http://player.vimeo.com/video/15243319" width="500" height="375" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p	2	Changed url.
16	2012-09-23 20:30:00.154187+10	1	9	4	English - South Park Parody of iPad Ad	2	No fields changed.
17	2012-09-23 20:30:47.16854+10	1	9	5	English - Simpsons - South Park parody	2	Changed url.
18	2012-09-23 20:31:20.483426+10	1	9	3	English - Homer lie detector	2	Changed url.
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	permission	auth	permission
2	group	auth	group
3	user	auth	user
4	content type	contenttypes	contenttype
5	session	sessions	session
6	site	sites	site
7	log entry	admin	logentry
8	language	listener	language
9	listener	listener	listener
10	accent	listener	accent
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
b40df17ed42e9b282401837856c6e79d	ZTFhYTY2YjcwODdlOGI5ZjRlZTVhOGYyYzE5OTNmMDZhNjgxMjM2ZTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n	2012-10-07 15:32:40.904328+11
\.


--
-- Data for Name: django_site; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY django_site (id, domain, name) FROM stdin;
1	example.com	example.com
\.


--
-- Data for Name: listener_accent; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY listener_accent (id, name, language_id) FROM stdin;
\.


--
-- Data for Name: listener_language; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY listener_language (id, name) FROM stdin;
1	English
2	Español
3	Italiano
\.


--
-- Data for Name: listener_listener; Type: TABLE DATA; Schema: public; Owner: adrian
--

COPY listener_listener (id, url, title, description, pub_date, update_date, broken, language_id, length) FROM stdin;
4	<iframe src="http://player.vimeo.com/video/15243319" width="500" height="375" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p><a href="http://vimeo.com/15243319">South Park Parody of iPad Ad</a> from <a href="http://vimeo.com/user4805530">Will Bramlett</a> on <a href="http://vimeo.com">Vimeo</a>.</p>	South Park Parody of iPad Ad		2012-09-23 20:01:41.805384+10	2012-09-23 20:30:00.147762+10	f	1	15
5	<iframe src="http://player.vimeo.com/video/8221814" width="500" height="375" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe> <p><a href="http://vimeo.com/8221814">I Simpson-parodia di South park</a> from <a href="http://vimeo.com/user2813437">videus</a> on <a href="http://vimeo.com">Vimeo</a>.</p>	Simpsons - South Park parody		2012-09-23 20:08:58.254906+10	2012-09-23 20:30:47.166532+10	f	1	35
3	<iframe width="420" height="315" src="http://www.youtube.com/embed/HqmHXnryakA" frameborder="0" allowfullscreen></iframe>	Homer lie detector		2012-09-23 15:35:59.565959+10	2012-09-23 20:31:20.481279+10	f	1	12
\.


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_model_key; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_key UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: django_site_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);


--
-- Name: listener_accent_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY listener_accent
    ADD CONSTRAINT listener_accent_pkey PRIMARY KEY (id);


--
-- Name: listener_language_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY listener_language
    ADD CONSTRAINT listener_language_pkey PRIMARY KEY (id);


--
-- Name: listener_listener_pkey; Type: CONSTRAINT; Schema: public; Owner: adrian; Tablespace: 
--

ALTER TABLE ONLY listener_listener
    ADD CONSTRAINT listener_listener_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions_group_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_group_permissions_group_id ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_group_permissions_permission_id ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_permission_content_type_id ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_user_groups_group_id ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_user_groups_user_id ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_permission_id ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_user_id ON auth_user_user_permissions USING btree (user_id);


--
-- Name: django_admin_log_content_type_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX django_admin_log_content_type_id ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX django_admin_log_user_id ON django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX django_session_expire_date ON django_session USING btree (expire_date);


--
-- Name: listener_accent_language_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX listener_accent_language_id ON listener_accent USING btree (language_id);


--
-- Name: listener_listener_language_id; Type: INDEX; Schema: public; Owner: adrian; Tablespace: 
--

CREATE INDEX listener_listener_language_id ON listener_listener USING btree (language_id);


--
-- Name: auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: content_type_id_refs_id_728de91f; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT content_type_id_refs_id_728de91f FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: group_id_refs_id_3cea63fe; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT group_id_refs_id_3cea63fe FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: listener_accent_language_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY listener_accent
    ADD CONSTRAINT listener_accent_language_id_fkey FOREIGN KEY (language_id) REFERENCES listener_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: listener_listener_language_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY listener_listener
    ADD CONSTRAINT listener_listener_language_id_fkey FOREIGN KEY (language_id) REFERENCES listener_language(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_7ceef80f; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT user_id_refs_id_7ceef80f FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: user_id_refs_id_dfbab7d; Type: FK CONSTRAINT; Schema: public; Owner: adrian
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT user_id_refs_id_dfbab7d FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

