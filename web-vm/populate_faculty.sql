-- Connect to the dashboard database created in init.sql
\c dashboard

-- Wipe existing rows
TRUNCATE TABLE public.faculty RESTART IDENTITY;

DO $$
BEGIN
    FOR i IN 1..105 LOOP
        -- Only use the 3 columns defined in your teammate's init.sql
        INSERT INTO public.faculty (name, department, email)
        VALUES (
            'Faculty Member ' || i,
            'Computer Science',
            'faculty' || i || '@ecu.edu'
        );
    END LOOP;
END $$;
