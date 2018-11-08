--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)
-- Dumped by pg_dump version 10.5 (Ubuntu 10.5-0ubuntu0.18.04)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: attachment; Type: TABLE; Schema: public; Owner: dmitry
--

CREATE TABLE public.attachment (
    attach_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    message_id integer NOT NULL,
    type text NOT NULL,
    url text NOT NULL
);


ALTER TABLE public.attachment OWNER TO dmitry;

--
-- Name: attachment_attach_id_seq; Type: SEQUENCE; Schema: public; Owner: dmitry
--

CREATE SEQUENCE public.attachment_attach_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attachment_attach_id_seq OWNER TO dmitry;

--
-- Name: attachment_attach_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dmitry
--

ALTER SEQUENCE public.attachment_attach_id_seq OWNED BY public.attachment.attach_id;


--
-- Name: chat; Type: TABLE; Schema: public; Owner: dmitry
--

CREATE TABLE public.chat (
    chat_id integer NOT NULL,
    is_group_chat boolean DEFAULT false,
    topic text,
    last_message text,
    CONSTRAINT chat_last_message_check CHECK ((length(last_message) < 65536))
);


ALTER TABLE public.chat OWNER TO dmitry;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE; Schema: public; Owner: dmitry
--

CREATE SEQUENCE public.chat_chat_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chat_chat_id_seq OWNER TO dmitry;

--
-- Name: chat_chat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dmitry
--

ALTER SEQUENCE public.chat_chat_id_seq OWNED BY public.chat.chat_id;


--
-- Name: member; Type: TABLE; Schema: public; Owner: dmitry
--

CREATE TABLE public.member (
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    new_messages bigint,
    last_read_message_id integer
);


ALTER TABLE public.member OWNER TO dmitry;

--
-- Name: messages; Type: TABLE; Schema: public; Owner: dmitry
--

CREATE TABLE public.messages (
    message_id integer NOT NULL,
    chat_id integer NOT NULL,
    user_id integer NOT NULL,
    content text NOT NULL,
    added_at timestamp without time zone DEFAULT now() NOT NULL,
    CONSTRAINT messages_content_check CHECK ((length(content) < 65536))
);


ALTER TABLE public.messages OWNER TO dmitry;

--
-- Name: messages_message_id_seq; Type: SEQUENCE; Schema: public; Owner: dmitry
--

CREATE SEQUENCE public.messages_message_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.messages_message_id_seq OWNER TO dmitry;

--
-- Name: messages_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dmitry
--

ALTER SEQUENCE public.messages_message_id_seq OWNED BY public.messages.message_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: dmitry
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    name text NOT NULL,
    nick text NOT NULL,
    avatar text,
    CONSTRAINT users_name_check CHECK ((length(name) < 32)),
    CONSTRAINT users_nick_check CHECK ((length(nick) < 32))
);


ALTER TABLE public.users OWNER TO dmitry;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: dmitry
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO dmitry;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dmitry
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: attachment attach_id; Type: DEFAULT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.attachment ALTER COLUMN attach_id SET DEFAULT nextval('public.attachment_attach_id_seq'::regclass);


--
-- Name: chat chat_id; Type: DEFAULT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.chat ALTER COLUMN chat_id SET DEFAULT nextval('public.chat_chat_id_seq'::regclass);


--
-- Name: messages message_id; Type: DEFAULT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.messages ALTER COLUMN message_id SET DEFAULT nextval('public.messages_message_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: attachment attachment_pkey; Type: CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.attachment
    ADD CONSTRAINT attachment_pkey PRIMARY KEY (attach_id);


--
-- Name: chat chat_pkey; Type: CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.chat
    ADD CONSTRAINT chat_pkey PRIMARY KEY (chat_id);


--
-- Name: messages messages_pkey; Type: CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_pkey PRIMARY KEY (message_id);


--
-- Name: users users_nick_key; Type: CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_nick_key UNIQUE (nick);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: attachment attachment_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.attachment
    ADD CONSTRAINT attachment_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chat(chat_id);


--
-- Name: attachment attachment_message_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.attachment
    ADD CONSTRAINT attachment_message_id_fkey FOREIGN KEY (message_id) REFERENCES public.messages(message_id);


--
-- Name: attachment attachment_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.attachment
    ADD CONSTRAINT attachment_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: member member_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chat(chat_id);


--
-- Name: member member_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: messages messages_chat_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_chat_id_fkey FOREIGN KEY (chat_id) REFERENCES public.chat(chat_id);


--
-- Name: messages messages_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: dmitry
--

ALTER TABLE ONLY public.messages
    ADD CONSTRAINT messages_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

