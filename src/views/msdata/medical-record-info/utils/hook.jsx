import { ElMessage, ElMessageBox } from "element-plus";
import { ref } from "vue";
import { deleteApi, pageApi, listApi } from "./api";
import {
  addDialog,
  closeDialog,
} from "@@/plugin-platform/components/dialog/hook";
import FormComponent from "../form.vue";
import { useSelect } from "@@/plugin-platform/utils/hooks";

/**
 * 
 * @param {Object} editOptions 
 * @param {String} editOptions.title 
 * @param {String} [editOptions.id] 
 * @param {import('./types').IMedicalRecordInfo} [editOptions.row]
 * @param {()=>void} [editOptions.effect] 
 */
export function handleEdit(editOptions) {
  const editRef = ref();
  const dialog = addDialog({
    effect: editOptions.effect,
    title: editOptions.title,
    props: editOptions,
    width: "40%",
    footerButtons: [
      {
        label: "重置",
        type: "info",
        btnClick: () => editRef.value.reset()
      },
      {
        label: "保存",
        type: "primary",
        btnClick: async () => {
          await editRef.value.submit();
          ElMessage.success("保存成功");
          closeDialog(dialog);
        }
      }
    ],
    contentRenderer: () => <FormComponent ref={editRef} />,
  });
}

/**
 * 
 * @param {string|string[]} ids 
 * @param {()=>void} [effect] 
 * @returns 
 */
export async function handleDelete(
  ids,
  effect
) {
  const callback = await ElMessageBox.confirm("确认删除？", "删除", { 
    showCancelButton: true
  });
  if (callback !== "confirm") return;
  const deleteId = Array.isArray(ids) ? ids.join(",") : ids;
  await deleteApi({ ids: deleteId });
  effect?.();
}

/**
 * 
 * @param {Object} editOptions 
 * @param {String} editOptions.title 
 * @param {String} [editOptions.id] 
 * @param {import('./types').IMedicalRecordInfo} [editOptions.row]
 * @param {()=>void} [editOptions.effect] 
 */
export function handleView(editOptions) {
  const viewRef = ref();
  addDialog({
    title: editOptions.title,
    props: editOptions,
    width: "40%",
    contentRenderer: () => <FormComponent ref={viewRef} readPretty />
  });
}


export function useMedicalRecordInfoSelect() {
  const { fetch, options, ...rest } = useSelect({
    default: [],
    fetch: async (blurry) => {
      const data = await listApi({ blurry });
      return data;
    },
  });
  return {
    ...rest,
    options,
    fetch: (blurry) => {
      if (!blurry) return options;
      return fetch(blurry);
    },
  };
}
