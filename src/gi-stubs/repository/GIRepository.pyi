from typing import Any
from typing import Literal
from typing import Optional
from typing import Union

from gi.repository import GObject

MAJOR_VERSION: int = ...
MICRO_VERSION: int = ...
MINOR_VERSION: int = ...
TYPE_TAG_N_TYPES: int = ...
_namespace: str = ...
_version: str = ...

def arg_info_get_closure(*args, **kwargs): ...
def arg_info_get_destroy(*args, **kwargs): ...
def arg_info_get_direction(*args, **kwargs): ...
def arg_info_get_ownership_transfer(*args, **kwargs): ...
def arg_info_get_scope(*args, **kwargs): ...
def arg_info_get_type(*args, **kwargs): ...
def arg_info_is_caller_allocates(*args, **kwargs): ...
def arg_info_is_optional(*args, **kwargs): ...
def arg_info_is_return_value(*args, **kwargs): ...
def arg_info_is_skip(*args, **kwargs): ...
def arg_info_load_type(*args, **kwargs): ...
def arg_info_may_be_null(*args, **kwargs): ...
def callable_info_can_throw_gerror(*args, **kwargs): ...
def callable_info_get_arg(*args, **kwargs): ...
def callable_info_get_caller_owns(*args, **kwargs): ...
def callable_info_get_instance_ownership_transfer(*args, **kwargs): ...
def callable_info_get_n_args(*args, **kwargs): ...
def callable_info_get_return_attribute(*args, **kwargs): ...
def callable_info_get_return_type(*args, **kwargs): ...
def callable_info_invoke(*args, **kwargs): ...
def callable_info_is_method(*args, **kwargs): ...
def callable_info_iterate_return_attributes(*args, **kwargs): ...
def callable_info_load_arg(*args, **kwargs): ...
def callable_info_load_return_type(*args, **kwargs): ...
def callable_info_may_return_null(*args, **kwargs): ...
def callable_info_skip_return(*args, **kwargs): ...
def cclosure_marshal_generic(*args, **kwargs): ...
def constant_info_get_type(*args, **kwargs): ...
def enum_info_get_error_domain(*args, **kwargs): ...
def enum_info_get_method(*args, **kwargs): ...
def enum_info_get_n_methods(*args, **kwargs): ...
def enum_info_get_n_values(*args, **kwargs): ...
def enum_info_get_storage_type(*args, **kwargs): ...
def enum_info_get_value(*args, **kwargs): ...
def field_info_get_flags(*args, **kwargs): ...
def field_info_get_offset(*args, **kwargs): ...
def field_info_get_size(*args, **kwargs): ...
def field_info_get_type(*args, **kwargs): ...
def function_info_get_flags(*args, **kwargs): ...
def function_info_get_property(*args, **kwargs): ...
def function_info_get_symbol(*args, **kwargs): ...
def function_info_get_vfunc(*args, **kwargs): ...
def get_major_version(*args, **kwargs): ...
def get_micro_version(*args, **kwargs): ...
def get_minor_version(*args, **kwargs): ...
def info_new(*args, **kwargs): ...
def info_type_to_string(*args, **kwargs): ...
def interface_info_find_method(*args, **kwargs): ...
def interface_info_find_signal(*args, **kwargs): ...
def interface_info_find_vfunc(*args, **kwargs): ...
def interface_info_get_constant(*args, **kwargs): ...
def interface_info_get_iface_struct(*args, **kwargs): ...
def interface_info_get_method(*args, **kwargs): ...
def interface_info_get_n_constants(*args, **kwargs): ...
def interface_info_get_n_methods(*args, **kwargs): ...
def interface_info_get_n_prerequisites(*args, **kwargs): ...
def interface_info_get_n_properties(*args, **kwargs): ...
def interface_info_get_n_signals(*args, **kwargs): ...
def interface_info_get_n_vfuncs(*args, **kwargs): ...
def interface_info_get_prerequisite(*args, **kwargs): ...
def interface_info_get_property(*args, **kwargs): ...
def interface_info_get_signal(*args, **kwargs): ...
def interface_info_get_vfunc(*args, **kwargs): ...
def invoke_error_quark(*args, **kwargs): ...
def object_info_find_method(*args, **kwargs): ...
def object_info_find_method_using_interfaces(*args, **kwargs): ...
def object_info_find_signal(*args, **kwargs): ...
def object_info_find_vfunc(*args, **kwargs): ...
def object_info_find_vfunc_using_interfaces(*args, **kwargs): ...
def object_info_get_abstract(*args, **kwargs): ...
def object_info_get_class_struct(*args, **kwargs): ...
def object_info_get_constant(*args, **kwargs): ...
def object_info_get_field(*args, **kwargs): ...
def object_info_get_fundamental(*args, **kwargs): ...
def object_info_get_get_value_function(*args, **kwargs): ...
def object_info_get_interface(*args, **kwargs): ...
def object_info_get_method(*args, **kwargs): ...
def object_info_get_n_constants(*args, **kwargs): ...
def object_info_get_n_fields(*args, **kwargs): ...
def object_info_get_n_interfaces(*args, **kwargs): ...
def object_info_get_n_methods(*args, **kwargs): ...
def object_info_get_n_properties(*args, **kwargs): ...
def object_info_get_n_signals(*args, **kwargs): ...
def object_info_get_n_vfuncs(*args, **kwargs): ...
def object_info_get_parent(*args, **kwargs): ...
def object_info_get_property(*args, **kwargs): ...
def object_info_get_ref_function(*args, **kwargs): ...
def object_info_get_set_value_function(*args, **kwargs): ...
def object_info_get_signal(*args, **kwargs): ...
def object_info_get_type_init(*args, **kwargs): ...
def object_info_get_type_name(*args, **kwargs): ...
def object_info_get_unref_function(*args, **kwargs): ...
def object_info_get_vfunc(*args, **kwargs): ...
def property_info_get_flags(*args, **kwargs): ...
def property_info_get_ownership_transfer(*args, **kwargs): ...
def property_info_get_type(*args, **kwargs): ...
def registered_type_info_get_g_type(*args, **kwargs): ...
def registered_type_info_get_type_init(*args, **kwargs): ...
def registered_type_info_get_type_name(*args, **kwargs): ...
def signal_info_get_class_closure(*args, **kwargs): ...
def signal_info_get_flags(*args, **kwargs): ...
def signal_info_true_stops_emit(*args, **kwargs): ...
def struct_info_find_field(*args, **kwargs): ...
def struct_info_find_method(*args, **kwargs): ...
def struct_info_get_alignment(*args, **kwargs): ...
def struct_info_get_field(*args, **kwargs): ...
def struct_info_get_method(*args, **kwargs): ...
def struct_info_get_n_fields(*args, **kwargs): ...
def struct_info_get_n_methods(*args, **kwargs): ...
def struct_info_get_size(*args, **kwargs): ...
def struct_info_is_foreign(*args, **kwargs): ...
def struct_info_is_gtype_struct(*args, **kwargs): ...
def type_info_argument_from_hash_pointer(*args, **kwargs): ...
def type_info_get_array_fixed_size(*args, **kwargs): ...
def type_info_get_array_length(*args, **kwargs): ...
def type_info_get_array_type(*args, **kwargs): ...
def type_info_get_interface(*args, **kwargs): ...
def type_info_get_param_type(*args, **kwargs): ...
def type_info_get_storage_type(*args, **kwargs): ...
def type_info_get_tag(*args, **kwargs): ...
def type_info_hash_pointer_from_argument(*args, **kwargs): ...
def type_info_is_pointer(*args, **kwargs): ...
def type_info_is_zero_terminated(*args, **kwargs): ...
def type_tag_to_string(*args, **kwargs): ...
def union_info_find_method(*args, **kwargs): ...
def union_info_get_alignment(*args, **kwargs): ...
def union_info_get_discriminator(*args, **kwargs): ...
def union_info_get_discriminator_offset(*args, **kwargs): ...
def union_info_get_discriminator_type(*args, **kwargs): ...
def union_info_get_field(*args, **kwargs): ...
def union_info_get_method(*args, **kwargs): ...
def union_info_get_n_fields(*args, **kwargs): ...
def union_info_get_n_methods(*args, **kwargs): ...
def union_info_get_size(*args, **kwargs): ...
def union_info_is_discriminated(*args, **kwargs): ...
def value_info_get_value(*args, **kwargs): ...
def vfunc_info_get_address(*args, **kwargs): ...
def vfunc_info_get_flags(*args, **kwargs): ...
def vfunc_info_get_invoker(*args, **kwargs): ...
def vfunc_info_get_offset(*args, **kwargs): ...
def vfunc_info_get_signal(*args, **kwargs): ...

class Argument:
    v_boolean = ...
    v_double = ...
    v_float = ...
    v_int = ...
    v_int16 = ...
    v_int32 = ...
    v_int64 = ...
    v_int8 = ...
    v_long = ...
    v_pointer = ...
    v_short = ...
    v_size = ...
    v_ssize = ...
    v_string = ...
    v_uint = ...
    v_uint16 = ...
    v_uint32 = ...
    v_uint64 = ...
    v_uint8 = ...
    v_ulong = ...
    v_ushort = ...

class AttributeIter:
    data = ...
    data2 = ...
    data3 = ...
    data4 = ...

class BaseInfo:
    dummy1 = ...
    dummy2 = ...
    dummy3 = ...
    dummy4 = ...
    dummy5 = ...
    dummy6 = ...
    dummy7 = ...
    padding = ...

    def equal(*args, **kwargs): ...
    def get_attribute(*args, **kwargs): ...
    def get_container(*args, **kwargs): ...
    def get_name(*args, **kwargs): ...
    def get_namespace(*args, **kwargs): ...
    def get_type(*args, **kwargs): ...
    def get_typelib(*args, **kwargs): ...
    def is_deprecated(*args, **kwargs): ...
    def iterate_attributes(*args, **kwargs): ...

class Repository:
    parent = ...
    priv = ...

    def dump(*args, **kwargs): ...
    def enumerate_versions(*args, **kwargs): ...
    def error_quark(*args, **kwargs): ...
    def find_by_error_domain(*args, **kwargs): ...
    def find_by_gtype(*args, **kwargs): ...
    def find_by_name(*args, **kwargs): ...
    def get_c_prefix(*args, **kwargs): ...
    def get_default(*args, **kwargs): ...
    def get_dependencies(*args, **kwargs): ...
    def get_immediate_dependencies(*args, **kwargs): ...
    def get_info(*args, **kwargs): ...
    def get_loaded_namespaces(*args, **kwargs): ...
    def get_n_infos(*args, **kwargs): ...
    def get_object_gtype_interfaces(*args, **kwargs): ...
    def get_option_group(*args, **kwargs): ...
    @classmethod
    def get_search_path(cls) -> list[str]: ...
    def get_shared_library(self, namespace: str) -> Optional[str]: ...
    def get_typelib_path(*args, **kwargs): ...
    def get_version(*args, **kwargs): ...
    def is_registered(*args, **kwargs): ...
    def load_typelib(*args, **kwargs): ...
    def prepend_library_path(*args, **kwargs): ...
    def prepend_search_path(*args, **kwargs): ...
    def require(
        self,
        namespace: str,
        version: Optional[str],
        flags: Union[RepositoryLoadFlags, Literal[0]],
    ) -> Any: ...
    def require_private(*args, **kwargs): ...

class Typelib:
    def free(*args, **kwargs): ...
    def get_namespace(*args, **kwargs): ...
    def symbol(*args, **kwargs): ...

class UnresolvedInfo: ...

class FieldInfoFlags(GObject.GFlags):
    READABLE = ...
    WRITABLE = ...

class FunctionInfoFlags(GObject.GFlags):
    IS_CONSTRUCTOR = ...
    IS_GETTER = ...
    IS_METHOD = ...
    IS_SETTER = ...
    THROWS = ...
    WRAPS_VFUNC = ...

class RepositoryLoadFlags(GObject.GFlags):
    IREPOSITORY_LOAD_FLAG_LAZY = ...

class VFuncInfoFlags(GObject.GFlags):
    MUST_CHAIN_UP = ...
    MUST_NOT_OVERRIDE = ...
    MUST_OVERRIDE = ...
    THROWS = ...

class ArrayType(GObject.GEnum):
    ARRAY = ...
    BYTE_ARRAY = ...
    C = ...
    PTR_ARRAY = ...

class Direction(GObject.GEnum):
    IN = ...
    INOUT = ...
    OUT = ...

class InfoType(GObject.GEnum):
    ARG = ...
    BOXED = ...
    CALLBACK = ...
    CONSTANT = ...
    ENUM = ...
    FIELD = ...
    FLAGS = ...
    FUNCTION = ...
    INTERFACE = ...
    INVALID = ...
    INVALID_0 = ...
    OBJECT = ...
    PROPERTY = ...
    SIGNAL = ...
    STRUCT = ...
    TYPE = ...
    UNION = ...
    UNRESOLVED = ...
    VALUE = ...
    VFUNC = ...

class RepositoryError(GObject.GEnum):
    LIBRARY_NOT_FOUND = ...
    NAMESPACE_MISMATCH = ...
    NAMESPACE_VERSION_CONFLICT = ...
    TYPELIB_NOT_FOUND = ...

class ScopeType(GObject.GEnum):
    ASYNC = ...
    CALL = ...
    INVALID = ...
    NOTIFIED = ...

class Transfer(GObject.GEnum):
    CONTAINER = ...
    EVERYTHING = ...
    NOTHING = ...

class TypeTag(GObject.GEnum):
    ARRAY = ...
    BOOLEAN = ...
    DOUBLE = ...
    ERROR = ...
    FILENAME = ...
    FLOAT = ...
    GHASH = ...
    GLIST = ...
    GSLIST = ...
    GTYPE = ...
    INT16 = ...
    INT32 = ...
    INT64 = ...
    INT8 = ...
    INTERFACE = ...
    UINT16 = ...
    UINT32 = ...
    UINT64 = ...
    UINT8 = ...
    UNICHAR = ...
    UTF8 = ...
    VOID = ...

class nvokeError(GObject.GEnum):
    ARGUMENT_MISMATCH = ...
    FAILED = ...
    SYMBOL_NOT_FOUND = ...
