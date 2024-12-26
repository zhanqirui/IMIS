CREATE OR REPLACE TRIGGER "MSDATA"."update_patient_visit"
AFTER INSERT ON "MSDATA"."patient_info"
FOR EACH ROW
BEGIN
    UPDATE "MSDATA"."hospital_info"
    SET "patient_visit" = "patient_visit" + 1;
END;
