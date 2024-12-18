CREATE OR REPLACE TRIGGER "${moduleSchema}"."kesplus_tr_module_package_lock" BEFORE DELETE OR UPDATE ON "${moduleSchema}"."kes_packages" FOR EACH ROW
declare
    user_id_ varchar;
    hold_lock_user_ varchar;
BEGIN
    user_id_ := "kesplus_platform".user('userId');
    if user_id_ is not null then
        select t.hold_lock_user into hold_lock_user_ from "kesplus_app"."kes_app_sql_property_lock" t where t.sql_property_id= old.id and t.sql_property_type = 4;
        if hold_lock_user_ != user_id_ then
            raise exception '请先获取编辑锁';
        end if;
    end if;
END;