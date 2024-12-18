CREATE OR REPLACE TRIGGER "${moduleSchema}"."kesplus_tr_module_role_policy" AFTER INSERT OR UPDATE OR DELETE ON "${moduleSchema}"."kesplus_module_role_policy" FOR EACH ROW
BEGIN
	IF TG_OP = 'insert' THEN
        INSERT INTO "kesplus_base"."kesplus_base_role_policy"(
            "id", "role_id", "policy_id", "create_by", "create_time", "update_by", "update_time", "dept_id", "module_id"
        )VALUES(
        	new."id", new."role_id", new."policy_id", new."create_by", new."create_time", new."update_by", new."update_time", new."dept_id", new."module_id"
        );
	ELSEIF TG_OP = 'update' THEN
		UPDATE "kesplus_base"."kesplus_base_role_policy"
        SET "role_id"=new."role_id", "policy_id"=new."policy_id", "update_by"=new."update_by", "update_time"=new."update_time"
        WHERE "id"=old."id";
	ELSE   --delete
		DELETE FROM "kesplus_base"."kesplus_base_role_policy" WHERE "id"=OLD.id;
	END IF;

END;