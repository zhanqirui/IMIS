CREATE OR REPLACE TRIGGER "${moduleSchema}"."kesplus_tr_module_role_permission" AFTER INSERT OR UPDATE OR DELETE ON "${moduleSchema}"."kesplus_module_role_permission" FOR EACH ROW
BEGIN
	IF TG_OP = 'insert' THEN
        INSERT INTO "kesplus_base"."kesplus_base_role_permission"(
            "id", "role_id", "permission_id", "create_by", "create_time", "update_by", "update_time", "dept_id", module_id
        )VALUES(
        	new."id", new."role_id", new."permission_id", new."create_by", new."create_time", new."update_by", new."update_time", new."dept_id", new.module_id
        );
	ELSEIF TG_OP = 'update' THEN
		UPDATE "kesplus_base"."kesplus_base_role_permission"
        SET "role_id"=new."role_id", "permission_id"=new."permission_id", "update_by"=new."update_by", "update_time"=new."update_time"
        WHERE "id"=old."id";
	ELSE   --delete
		DELETE FROM "kesplus_base"."kesplus_base_role_permission" WHERE "id"=OLD.id;
	END IF;

END;