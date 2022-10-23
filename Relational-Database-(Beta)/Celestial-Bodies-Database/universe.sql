--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-2.pgdg20.04+1)

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

DROP DATABASE universe;
--
-- Name: universe; Type: DATABASE; Schema: -; Owner: freecodecamp
--

CREATE DATABASE universe WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8';


ALTER DATABASE universe OWNER TO freecodecamp;

\connect universe

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
-- Name: galaxy; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.galaxy (
    galaxy_id integer NOT NULL,
    name character varying(30) NOT NULL,
    age integer,
    radius integer,
    mass integer
);


ALTER TABLE public.galaxy OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.galaxy_galaxy_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.galaxy_galaxy_id_seq OWNER TO freecodecamp;

--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.galaxy_galaxy_id_seq OWNED BY public.galaxy.galaxy_id;


--
-- Name: lifeform; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.lifeform (
    name character varying(30) NOT NULL,
    lifeform_id integer NOT NULL,
    lifespan integer
);


ALTER TABLE public.lifeform OWNER TO freecodecamp;

--
-- Name: lifeforms_lifeform_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.lifeforms_lifeform_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lifeforms_lifeform_id_seq OWNER TO freecodecamp;

--
-- Name: lifeforms_lifeform_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.lifeforms_lifeform_id_seq OWNED BY public.lifeform.lifeform_id;


--
-- Name: moon; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.moon (
    moon_id integer NOT NULL,
    name character varying(30) NOT NULL,
    planet_id integer,
    description text,
    orbital_distance integer,
    has_life boolean
);


ALTER TABLE public.moon OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.moon_moon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.moon_moon_id_seq OWNER TO freecodecamp;

--
-- Name: moon_moon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.moon_moon_id_seq OWNED BY public.moon.moon_id;


--
-- Name: planet; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.planet (
    planet_id integer NOT NULL,
    name character varying(30) NOT NULL,
    star_id integer,
    description text,
    distance_from_star numeric(8,1),
    has_life boolean
);


ALTER TABLE public.planet OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.planet_planet_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planet_planet_id_seq OWNER TO freecodecamp;

--
-- Name: planet_planet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.planet_planet_id_seq OWNED BY public.planet.planet_id;


--
-- Name: star; Type: TABLE; Schema: public; Owner: freecodecamp
--

CREATE TABLE public.star (
    star_id integer NOT NULL,
    name character varying(30) NOT NULL,
    galaxy_id integer,
    distance_from_sol numeric(4,1),
    type character(1)
);


ALTER TABLE public.star OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE; Schema: public; Owner: freecodecamp
--

CREATE SEQUENCE public.star_star_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.star_star_id_seq OWNER TO freecodecamp;

--
-- Name: star_star_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: freecodecamp
--

ALTER SEQUENCE public.star_star_id_seq OWNED BY public.star.star_id;


--
-- Name: galaxy galaxy_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy ALTER COLUMN galaxy_id SET DEFAULT nextval('public.galaxy_galaxy_id_seq'::regclass);


--
-- Name: lifeform lifeform_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.lifeform ALTER COLUMN lifeform_id SET DEFAULT nextval('public.lifeforms_lifeform_id_seq'::regclass);


--
-- Name: moon moon_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon ALTER COLUMN moon_id SET DEFAULT nextval('public.moon_moon_id_seq'::regclass);


--
-- Name: planet planet_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet ALTER COLUMN planet_id SET DEFAULT nextval('public.planet_planet_id_seq'::regclass);


--
-- Name: star star_id; Type: DEFAULT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star ALTER COLUMN star_id SET DEFAULT nextval('public.star_star_id_seq'::regclass);


--
-- Data for Name: galaxy; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.galaxy VALUES (1, 'Milky Way', 14, 20, 133);
INSERT INTO public.galaxy VALUES (2, 'Republic', 7, 12, 53);
INSERT INTO public.galaxy VALUES (3, 'Andromeda', 12, 23, 443);
INSERT INTO public.galaxy VALUES (4, 'Garbok', 122, 2233, 4243);
INSERT INTO public.galaxy VALUES (5, 'Vibros', 2, 10, 33);
INSERT INTO public.galaxy VALUES (6, 'Misk', 123, 3, 2);


--
-- Data for Name: lifeform; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.lifeform VALUES ('Human', 1, 110);
INSERT INTO public.lifeform VALUES ('Thargoid', 2, NULL);
INSERT INTO public.lifeform VALUES ('Obelisks', 3, 2400);


--
-- Data for Name: moon; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.moon VALUES (1, 'Luna', 1, 'Rocks and dust make such a pretty nightlight.', 238900, false);
INSERT INTO public.moon VALUES (2, 'Phobos', 2, 'Fear.', 28900, false);
INSERT INTO public.moon VALUES (3, 'Deimos', 2, 'Panic.', 22900, false);
INSERT INTO public.moon VALUES (4, 'Centax-1', 3, 'Colonized.', 121231, true);
INSERT INTO public.moon VALUES (5, 'Centax-2', 3, 'Colonized.', 141231, true);
INSERT INTO public.moon VALUES (6, 'Centax-3', 3, 'Colonized.', 1478631, true);
INSERT INTO public.moon VALUES (7, 'Hesperidium', 3, 'A new home.', 8631, true);
INSERT INTO public.moon VALUES (8, 'LHS 20 A 1 A', 4, 'Rocky satellite.', 3631, true);
INSERT INTO public.moon VALUES (9, 'LHS 20 A 1 B', 4, 'Rocky satellite.', 7331, true);
INSERT INTO public.moon VALUES (10, 'LHS 20 A 1 C', 4, 'Icy satellite.', 73231, true);
INSERT INTO public.moon VALUES (11, 'LHS 20 A 2 A', 5, 'Icy satellite.', 7331, true);
INSERT INTO public.moon VALUES (12, 'LHS 20 A 2 B', 5, 'Rocky satellite.', 7392, true);
INSERT INTO public.moon VALUES (13, 'LHS 20 A 2 C', 5, 'Rocky satellite.', 73912, true);
INSERT INTO public.moon VALUES (14, 'LHS 20 A 2 D', 5, 'Rocky satellite. Barely in orbit.', 739172, true);
INSERT INTO public.moon VALUES (15, 'LHS 20 A 4 a', 5, 'Icy sattelite.', 772, true);
INSERT INTO public.moon VALUES (16, 'LHS 20 A 4 b', 5, 'Icy sattelite.', 7172, true);
INSERT INTO public.moon VALUES (17, 'LHS 20 A 4 c', 5, 'Icy sattelite.', 71712, true);
INSERT INTO public.moon VALUES (18, 'Franklins Inheritance', 7, 'Rodriga Franklin, Daughter of Geraldine, owns this now.', 73612, true);
INSERT INTO public.moon VALUES (19, 'Otomatone', 10, 'Moon music lulled us to sleep.', 7312, true);
INSERT INTO public.moon VALUES (20, 'Okidokie', 11, 'With eyes on her, all was well.', 735852, true);


--
-- Data for Name: planet; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.planet VALUES (1, 'Earth', 1, 'Only habitable Sol planet. Home to humanity.', 499.0, true);
INSERT INTO public.planet VALUES (2, 'Mars', 1, 'Rocky red soil. Terraformable. Closest planet to Earth.', 760.2, false);
INSERT INTO public.planet VALUES (3, 'Coruscant', 2, 'Panopolis. Seat of the Galactic Senate. Home to the Jedi Temple.', 523.2, true);
INSERT INTO public.planet VALUES (4, 'LHS 20 A 1', 3, 'Small rocky body. No native life, but humans have settled it.', 220.2, true);
INSERT INTO public.planet VALUES (5, 'LHS 20 A 3', 3, 'Large icy body with rings. Lucrative mining operations.', 1232.2, false);
INSERT INTO public.planet VALUES (6, 'LHS 20 A 4', 3, 'Large gas giant. No sign of life.', 4332.2, false);
INSERT INTO public.planet VALUES (7, 'Franklins Keep', 4, 'Geraldine Franklin colonized this body in 3023.', 332.2, true);
INSERT INTO public.planet VALUES (8, 'Sigint', 4, 'Site of the battle of ecclesiastes. No current residents.', 642.2, false);
INSERT INTO public.planet VALUES (9, 'Barre', 4, 'Old rebel bases all over the place. Half the surface was glassed.', 1642.2, false);
INSERT INTO public.planet VALUES (10, 'Omicron', 5, 'No longer traveled. Dangerous. Void creatures.', 12.2, true);
INSERT INTO public.planet VALUES (11, 'Omega', 5, 'No longer traveled. Dangerous. Void creatures.', 1332.2, true);
INSERT INTO public.planet VALUES (12, 'Omigosh', 5, 'No longer traveled. Dangerous. Valley girls.', 133232.2, true);


--
-- Data for Name: star; Type: TABLE DATA; Schema: public; Owner: freecodecamp
--

INSERT INTO public.star VALUES (1, 'Sol', 1, 0.0, 'G');
INSERT INTO public.star VALUES (2, 'Coruscant', 2, 999.0, 'B');
INSERT INTO public.star VALUES (3, 'LHS 20', 1, 50.4, 'M');
INSERT INTO public.star VALUES (4, 'Franklins Rest', 3, 999.9, 'A');
INSERT INTO public.star VALUES (5, 'Oberon', 4, 999.9, 'O');
INSERT INTO public.star VALUES (6, 'Bisk', 6, 999.9, 'T');


--
-- Name: galaxy_galaxy_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.galaxy_galaxy_id_seq', 6, true);


--
-- Name: lifeforms_lifeform_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.lifeforms_lifeform_id_seq', 3, true);


--
-- Name: moon_moon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.moon_moon_id_seq', 20, true);


--
-- Name: planet_planet_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.planet_planet_id_seq', 12, true);


--
-- Name: star_star_id_seq; Type: SEQUENCE SET; Schema: public; Owner: freecodecamp
--

SELECT pg_catalog.setval('public.star_star_id_seq', 6, true);


--
-- Name: galaxy galaxy_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_name_key UNIQUE (name);


--
-- Name: galaxy galaxy_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.galaxy
    ADD CONSTRAINT galaxy_pkey PRIMARY KEY (galaxy_id);


--
-- Name: lifeform lifeform_name_unique; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.lifeform
    ADD CONSTRAINT lifeform_name_unique UNIQUE (name);


--
-- Name: lifeform lifeforms_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.lifeform
    ADD CONSTRAINT lifeforms_pkey PRIMARY KEY (lifeform_id);


--
-- Name: moon moon_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_name_key UNIQUE (name);


--
-- Name: moon moon_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_pkey PRIMARY KEY (moon_id);


--
-- Name: planet planet_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_name_key UNIQUE (name);


--
-- Name: planet planet_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_pkey PRIMARY KEY (planet_id);


--
-- Name: star star_name_key; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_name_key UNIQUE (name);


--
-- Name: star star_pkey; Type: CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_pkey PRIMARY KEY (star_id);


--
-- Name: moon moon_planet_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.moon
    ADD CONSTRAINT moon_planet_id_fkey FOREIGN KEY (planet_id) REFERENCES public.planet(planet_id);


--
-- Name: planet planet_star_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.planet
    ADD CONSTRAINT planet_star_id_fkey FOREIGN KEY (star_id) REFERENCES public.star(star_id);


--
-- Name: star star_galaxy_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: freecodecamp
--

ALTER TABLE ONLY public.star
    ADD CONSTRAINT star_galaxy_id_fkey FOREIGN KEY (galaxy_id) REFERENCES public.galaxy(galaxy_id);


--
-- PostgreSQL database dump complete
--
