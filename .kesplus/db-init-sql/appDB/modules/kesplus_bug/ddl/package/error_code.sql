CREATE OR REPLACE PACKAGE "kesplus_bug"."error_code" AUTHID CURRENT_USER AS
    QUESTION_ID_NULL CONSTANT TEXT := 'kesplus_bug_1000';
    QUESTION_NO_EXIST CONSTANT TEXT := 'kesplus_bug_1001'; 
    QUESTION_STATUS_UNKNOWN CONSTANT TEXT := 'kesplus_bug_1002';
    QUESTION_NO_PERMISSION CONSTANT TEXT := 'kesplus_bug_1003';
end;

CREATE OR REPLACE PACKAGE BODY "kesplus_bug"."error_code" AS WRAPPED
/BI7rN81Kb9WpM8RmlhM/w==
END;

