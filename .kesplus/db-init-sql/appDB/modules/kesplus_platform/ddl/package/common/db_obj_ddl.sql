CREATE OR REPLACE PACKAGE "kesplus_platform"."db_obj_ddl" AUTHID CURRENT_USER AS
    /**
     * @Description 获取包的ddl语句
     * @param schemaName_ 模式名
     * @param pkgName_ 包名
     * @param type_ 导出类型 type_: header, body, all(header,body)
     * @Return text
     */
	function get_pkg_ddl(schemaName_ varchar,pkgName_ varchar,type_ varchar) return text;
    /**
     * @Description 获取包体内容（不包含create语句）json分别返回两部分（pkgspecsrc,pkgbodysrc）
     * @param schemaName_ 模式名
     * @param pkgName_ 包名
     * @Return json
     */
    function get_pkg_src(schemaName_ varchar,pkgName_ varchar) return json;
    /**
     * @Description 获取函数的完整ddl语句（多个函数名称相同的不能使用此方法）
     * @param schemaName_ 模式名
     * @param funName_ 函数名
     * @Return text
     */
	function get_fun_ddl(schemaName_ varchar,funName_ varchar) return text;
    /**
     * @Description 获取视图完整ddl语句
     * @param schemaName_ 模式名
     * @param viewName_ 函数名
     * @Return text
     */
    function get_view_ddl(schemaName_ varchar,viewName_ varchar) return text;
    /**
     * @Description 获取视图查询体内容（不包含create语句）
     * @param schemaName_ 模式名
     * @param viewName_ 函数名
     * @Return text
     */
    function get_view_src(schemaName_ varchar,viewName_ varchar) return text;
    /**
     * 根据schemaName遍历所有的table，然后关闭所有表的约束
     * 返回成功或者失败
     */
    FUNCTION disableConstraintBySchema(schemaNames_ varchar) return boolean ;
    /**
     * 根据schemaName遍历所有的table，然后启动所有表的约束
     * 返回成功或者失败
     */
    FUNCTION enableConstraintBySchema(schemaNames_ varchar) return boolean;
    FUNCTION alterConstraintBySchema(schemaNames_ varchar,opt varchar)  return boolean;
	BR VARCHAR := E'\n';
	TAB VARCHAR := E'\t';
	PKG_HEADER_TEMPLATE varchar := 'CREATE OR REPLACE PACKAGE "{{&schemaName}}"."{{&pkgName}}" AS';
	PKG_BODY_TEMPLATE varchar := 'CREATE OR REPLACE PACKAGE BODY "{{&schemaName}}"."{{&pkgName}}" AS';
    VIEW_TEMPLATE varchar := 'create or replace view "%s"."%s" as' || chr(10) || '  ';
end;

CREATE OR REPLACE PACKAGE BODY "kesplus_platform"."db_obj_ddl" AS WRAPPED
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
ZGETIANR9tLLQH3f3I8FBdxTD0Pm5G5Eel+f
END;

