# Only libraries are obfuscated: the navigation graph, Gecko and others find our classes by name, and renaming them
# crashes the app at startup.
-keepnames class org.mozilla.** { *; }
-keepnames class mozilla.** { *; }
-keepnames class org.yaml.snakeyaml.** { *; }

####################################################################################################
# JNA: the Rust bindings look up native symbols and struct fields by their Java names
####################################################################################################

-keep class com.sun.jna.** { *; }
-keep class * implements com.sun.jna.** { *; }

####################################################################################################
# Keep Fenix names readable in stack traces, while still allowing R8 to shrink and optimize Fenix
####################################################################################################

-keep,allowshrinking,allowoptimization class org.mozilla.fenix.** { *; }

####################################################################################################
# GeckoView built-ins
####################################################################################################

-dontwarn org.mozilla.geckoview.**

# Raptor now writes a *-config.yaml file to specify Gecko runtime settings (e.g. the profile dir). This
# file gets deserialized into a DebugConfig object, which is why we need to keep this class
# and its members.
-keep class org.mozilla.gecko.util.DebugConfig { *; }

####################################################################################################
# Remove debug logs from release builds
####################################################################################################
-assumenosideeffects class android.util.Log {
    public static boolean isLoggable(java.lang.String, int);
    public static int v(...);
    public static int d(...);
}

####################################################################################################
# Mozilla Application Services
####################################################################################################

-keep class mozilla.appservices.** { *; }

# Keep code generated from Glean Metrics
-keep class org.mozilla.fenix.GleanMetrics.** {  *; }
