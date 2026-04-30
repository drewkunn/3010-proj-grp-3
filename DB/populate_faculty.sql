-- Clean out the old test data first
TRUNCATE TABLE public.faculty RESTART IDENTITY;

-- Insert 105 Faculty Members using a loop
DO $$
BEGIN
    FOR i IN 1..105 LOOP
        INSERT INTO public.faculty (name, rank, email, phone, office)
        VALUES (
            'Faculty Member ' || i, 
            CASE 
                WHEN i % 3 = 0 THEN 'Professor'
                WHEN i % 3 = 1 THEN 'Associate Professor'
                ELSE 'Assistant Professor'
            END,
            'faculty' || i || '@ecu.edu',
            '252-328-' || LPAD(i::text, 4, '0'),
            'Science Bldg ' || (100 + i)
        );
    END LOOP;
END $$;
