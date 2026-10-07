package org.tgcv.viatra.v002.observer;

import java.io.InputStream;
import java.net.URL;
import org.eclipse.emf.common.util.URI;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.viatra.query.patternlanguage.emf.EMFPatternLanguageStandaloneSetup;
import org.eclipse.viatra.query.patternlanguage.emf.util.IClassLoaderProvider;

import com.google.inject.Guice;
import com.google.inject.Injector;

/**
 * VIATRA 2.0.2 standalone parser setup with the observer bundle classloader.
 */
public final class ObserverPatternParserSetup extends EMFPatternLanguageStandaloneSetup {

    public Injector createObserverInjector() {
        System.out.println("TGCV_CREATE_INJECTOR_DIAGNOSTIC=beforeGuiceCreateInjector");

        ClassLoader loader = ObserverPatternParserSetup.class.getClassLoader();
        System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=loader=" + loader);

        String resourceName = "org/eclipse/xtext/xbase/Xtype.xtextbin";
        System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=resource=" + resourceName);

        try {
            URL resourceUrl = loader == null ? null : loader.getResource(resourceName);
            System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=resourceUrl=" + resourceUrl);

            if (resourceUrl != null) {
                try (InputStream in = resourceUrl.openStream()) {
                    byte[] head = new byte[16];
                    int n = in.read(head);
                    StringBuilder hex = new StringBuilder();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) hex.append(' ');
                        hex.append(String.format("%02x", head[i] & 0xff));
                    }
                    System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=resourceHead=" + hex);
                    System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=resourceReadable=true");
                }
            } else {
                System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=resourceReadable=false");
            }
        } catch (Throwable t) {
            System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=exception=" +
                t.getClass().getName());
            System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=message=" +
                String.valueOf(t.getMessage()));
            Throwable cause = t.getCause();
            int depth = 0;
            while (cause != null && depth < 8) {
                System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=cause" + depth +
                    "=" + cause.getClass().getName() + ":" + String.valueOf(cause.getMessage()));
                cause = cause.getCause();
                depth++;
            }
        }

        System.out.println("TGCV_DIRECT_XTEXT_RESOURCE_DIAGNOSTIC=END");

        System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=begin");
        try {
            Class<?> xtypeClass = Class.forName(
                "org.eclipse.xtext.xbase.services.XtypeGrammarAccess",
                false,
                ObserverPatternParserSetup.class.getClassLoader());
            ClassLoader xtypeLoader = xtypeClass.getClassLoader();
            System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=class=" + xtypeClass.getName());
            System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=classLoader=" + xtypeLoader);
            URL xtypeResource = xtypeLoader == null ? null :
                xtypeLoader.getResource(resourceName);
            System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=resourceUrl=" + xtypeResource);
            if (xtypeResource != null) {
                try (InputStream in = xtypeResource.openStream()) {
                    byte[] head = new byte[16];
                    int n = in.read(head);
                    StringBuilder hex = new StringBuilder();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) hex.append(' ');
                        hex.append(String.format("%02x", head[i] & 0xff));
                    }
                    System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=resourceHead=" + hex);
                    System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=resourceReadable=true");
                }
            } else {
                System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=resourceReadable=false");
            }
        } catch (Throwable t) {
            System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=exception=" +
                t.getClass().getName());
            System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=message=" +
                String.valueOf(t.getMessage()));
        }
        System.out.println("TGCV_XTYPE_CLASS_DIAGNOSTIC=END");

        System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=begin");
        try {
            ClassLoader contextLoader = Thread.currentThread().getContextClassLoader();
            System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=loader=" + contextLoader);
            URL contextResource = contextLoader == null ? null :
                contextLoader.getResource(resourceName);
            System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=resourceUrl=" + contextResource);
            try {
                Class<?> contextXtypeClass = Class.forName(
                    "org.eclipse.xtext.xbase.services.XtypeGrammarAccess",
                    false,
                    contextLoader);
                System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=classLoader=" +
                    contextXtypeClass.getClassLoader());
                System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=classFound=true");
            } catch (Throwable t) {
                System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=classFound=false");
                System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=classException=" +
                    t.getClass().getName());
                System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=classMessage=" +
                    String.valueOf(t.getMessage()));
            }
        } catch (Throwable t) {
            System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=exception=" +
                t.getClass().getName());
            System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=message=" +
                String.valueOf(t.getMessage()));
        }
        System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=begin");
        try {
            ClassLoader resolverLoader = EMFPatternLanguageStandaloneSetup.class.getClassLoader();
            Class<?> resolverClass = Class.forName(
                "org.eclipse.xtext.resource.ClassloaderClasspathUriResolver", false, resolverLoader);
            Object resolver = resolverClass.getDeclaredConstructor().newInstance();
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=loader=" + resolverLoader);
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=resolverClass=" + resolverClass.getName());
            URI inputUri = URI.createURI("classpath:/org/eclipse/xtext/xbase/Xtype.xtextbin");
            java.lang.reflect.Method findMethod = resolverClass.getMethod(
                "findResourceOnClasspath", ClassLoader.class, URI.class);
            URI resolvedUri = (URI) findMethod.invoke(resolver, resolverLoader, inputUri);
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=inputUri=" + inputUri);
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=resolvedUri=" + resolvedUri);
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=resolvedScheme=" +
                (resolvedUri == null ? null : resolvedUri.scheme()));
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=resolvedExists=" +
                (resolvedUri != null && resolverLoader.getResource(resolvedUri.path()) != null));
            for (java.lang.reflect.Method method : resolverClass.getMethods()) {
                if (method.getName().equals("resolve") || method.getName().equals("findResourceOnClasspath")) {
                    System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=method=" + method);
                }
            }
        } catch (Throwable t) {
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=exception=" + t.getClass().getName());
            System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=message=" + String.valueOf(t.getMessage()));
        }
        System.out.println("TGCV_CLASSPATH_URI_RESOLVER_DIAGNOSTIC=END");

        System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=begin");
        try {
            ClassLoader resourceSetLoader = EMFPatternLanguageStandaloneSetup.class.getClassLoader();
            Class<?> resourceSetClass = Class.forName(
                "org.eclipse.xtext.resource.XtextResourceSet", false, resourceSetLoader);
            Object resourceSet = resourceSetClass.getDeclaredConstructor().newInstance();
            URI inputUri = URI.createURI("classpath:/org/eclipse/xtext/xbase/Xtype.xtextbin");

            java.lang.reflect.Method setContext = resourceSetClass.getMethod(
                "setClasspathURIContext", Object.class);
            setContext.invoke(resourceSet, resourceSetLoader);

            java.lang.reflect.Method getConverter = resourceSetClass.getMethod("getURIConverter");
            Object converter = getConverter.invoke(resourceSet);
            java.lang.reflect.Method normalize = converter.getClass().getMethod("normalize", URI.class);
            URI normalized = (URI) normalize.invoke(converter, inputUri);

            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=resourceSetClass=" +
                resourceSetClass.getName());
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=contextLoader=" +
                resourceSetLoader);
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=inputUri=" + inputUri);
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=normalizedUri=" + normalized);
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=normalizedScheme=" +
                (normalized == null ? null : normalized.scheme()));

            java.lang.reflect.Method getResource = resourceSetClass.getMethod(
                "getResource", URI.class, boolean.class);
            try {
                Object resource = getResource.invoke(resourceSet, normalized, false);
                System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=existingResource=" +
                    (resource != null ? resource.getClass().getName() : "null"));
            } catch (Throwable t) {
                Throwable c = t.getCause() == null ? t : t.getCause();
                System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=getResourceException=" +
                    c.getClass().getName());
                System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=getResourceMessage=" +
                    String.valueOf(c.getMessage()));
            }
        } catch (Throwable t) {
            Throwable c = t.getCause() == null ? t : t.getCause();
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=exception=" +
                c.getClass().getName());
            System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=message=" +
                String.valueOf(c.getMessage()));
        }
        System.out.println("TGCV_XTEXT_RESOURCESET_DIAGNOSTIC=END");

        System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=begin");
        try {
            ClassLoader patternLanguageLoader =
                EMFPatternLanguageStandaloneSetup.class.getClassLoader();
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=loader=" +
                patternLanguageLoader);

            Class<?> patternXtypeClass = Class.forName(
                "org.eclipse.xtext.xbase.services.XtypeGrammarAccess",
                false,
                patternLanguageLoader);
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=classFound=true");
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=classLoader=" +
                patternXtypeClass.getClassLoader());

            URL patternResource = patternLanguageLoader == null ? null :
                patternLanguageLoader.getResource(resourceName);
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=resourceUrl=" +
                patternResource);

            if (patternResource != null) {
                try (InputStream in = patternResource.openStream()) {
                    byte[] head = new byte[16];
                    int n = in.read(head);
                    StringBuilder hex = new StringBuilder();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) hex.append(' ');
                        hex.append(String.format("%02x", head[i] & 0xff));
                    }
                    System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=resourceHead=" +
                        hex);
                    System.out.println(
                        "TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=resourceReadable=true");
                }
            } else {
                System.out.println(
                    "TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=resourceReadable=false");
            }
        } catch (Throwable t) {
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=exception=" +
                t.getClass().getName());
            System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=message=" +
                String.valueOf(t.getMessage()));
        }
        System.out.println("TGCV_PATTERNLANGUAGE_CLASSLOADER_DIAGNOSTIC=END");

        System.out.println("TGCV_CONTEXT_CLASSLOADER_DIAGNOSTIC=END");

        System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=begin");
        try {
            org.eclipse.emf.ecore.resource.Resource.Factory.Registry registry =
                org.eclipse.emf.ecore.resource.Resource.Factory.Registry.INSTANCE;
            Object extensionFactory = registry.getExtensionToFactoryMap().get("xtextbin");
            System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=extensionFactory=" +
                (extensionFactory == null ? "null" : extensionFactory.getClass().getName()));
            Object defaultFactory = registry.getExtensionToFactoryMap().get("*");
            System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=defaultFactory=" +
                (defaultFactory == null ? "null" : defaultFactory.getClass().getName()));
            org.eclipse.emf.common.util.URI xtextbinUri =
                org.eclipse.emf.common.util.URI.createURI("classpath:/org/eclipse/xtext/xbase/Xtype.xtextbin");
            org.eclipse.emf.ecore.resource.Resource.Factory factory =
                registry.getEFactory(xtextbinUri);
            System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=uriFactory=" +
                (factory == null ? "null" : factory.getClass().getName()));
        } catch (Throwable t) {
            System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=exception=" + t.getClass().getName());
            System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=message=" + String.valueOf(t.getMessage()));
        }
        System.out.println("TGCV_XTEXTBIN_FACTORY_DIAGNOSTIC=END");

        ClassLoader previousContextLoader = Thread.currentThread().getContextClassLoader();
        ClassLoader patternLanguageLoader =
            EMFPatternLanguageStandaloneSetup.class.getClassLoader();
        try {
            Thread.currentThread().setContextClassLoader(patternLanguageLoader);
            System.out.println("TGCV_GUICE_CONTEXT_CLASSLOADER_DIAGNOSTIC=loader=" +
                Thread.currentThread().getContextClassLoader());

            Injector injector = Guice.createInjector(new ObserverParserModule());
            register(injector);
            return injector;
        } finally {
            Thread.currentThread().setContextClassLoader(previousContextLoader);
            System.out.println("TGCV_GUICE_CONTEXT_CLASSLOADER_DIAGNOSTIC=restored=" +
                Thread.currentThread().getContextClassLoader());
        }
    }

    public static final class ObserverParserModule extends StandaloneParserModule {
        @Override
        public Class<? extends IClassLoaderProvider> bindIClassLoaderProvider() {
            return ObserverClassLoaderProvider.class;
        }
    }

    public static final class ObserverClassLoaderProvider
            implements IClassLoaderProvider {
        @Override
        public ClassLoader getClassLoader(EObject context) {
            ClassLoader loader =
                EMFPatternLanguageStandaloneSetup.class.getClassLoader();
            if (loader == null) {
                throw new IllegalStateException(
                    "Observer bundle classloader is unavailable");
            }

            String resourceName = "org/eclipse/xtext/xbase/Xtype.xtextbin";
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=loader=" + loader.getClass().getName());
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=loaderToString=" + loader);
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resource=" + resourceName);
            java.net.URL resource = loader.getResource(resourceName);
            System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceUrl=" + resource);

            if (resource != null) {
                try (InputStream in = resource.openStream()) {
                    byte[] head = new byte[16];
                    int n = in.read(head);
                    StringBuilder hex = new StringBuilder();
                    for (int i = 0; i < n; i++) {
                        if (i > 0) hex.append(' ');
                        hex.append(String.format("%02x", head[i] & 0xff));
                    }
                    System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceHead=" + hex);
                } catch (Exception e) {
                    System.out.println("TGCV_CLASSLOADER_DIAGNOSTIC=resourceReadError=" +
                        e.getClass().getName() + ":" + e.getMessage());
                }
            }

            return loader;
        }
    }
}
